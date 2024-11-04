from utils import *
from tqdm import tqdm
from dataset import *
from concurrent.futures import ProcessPoolExecutor
import json
from functools import partial
import os

api_key = "your api key"

experiment = [
    (2, 12),
    (3, 8),
    (4, 6),
    (6, 4),
    (8, 3),
    (12, 2)
]

data_field = "college_mathematics" # change this to other fields

for n_participant, n_round in experiment:
    correct = []
    json_write = []

    dataloader = mmlu(data_field)
    length = next(dataloader)

    print(f"n_participant: {n_participant}, n_round: {n_round}")

    if(os.path.isfile(f"results/{data_field}_{n_participant}_{n_round}.json")):
        json_write = json.load(open(f"results/{data_field}_{n_participant}_{n_round}.json", "r"))
        length_already = len(json_write)
        length -= length_already
        for i in range(length_already):
            next(dataloader)
            correct.append(json_write[i][1])
        

    for question, ground_truth in tqdm(dataloader, total=length):
        opinions = ["" for _ in range(n_participant)]
        messages_list = [[{"role": "system", "content": system_prompt}] for _ in range(n_participant)]

        for round in range(n_round):
            if round == 0:
                prompt = [prompt1(question)] * n_participant
            else:
                prompt = prompt2(round, opinions)
            
            with ProcessPoolExecutor(4) as executor:
                futures = []
                for i in range(n_participant):
                    messages_list[i].append({"role": "user", "content": prompt[i]})
                    task = partial(chatgpt, messages_list[i], api_key)
                    futures.append(executor.submit(task))
                for i in range(n_participant):
                    opinions[i] = futures[i].result()
                    messages_list[i].append({"role": "assistant", "content": opinions[i]})
            
            # print(round)

        answers = [extract_answer(question, opinion, api_key) for opinion in opinions]

        score = [score_answer(question, ground_truth, answer, api_key) for answer in answers]
        correct.append(True if score.count(1) >= score.count(0) else False)

        json_write.append([messages_list, correct])
        json.dump(json_write, open(f"results/{data_field}_{n_participant}_{n_round}.json", "w"), ensure_ascii=False)

    print(f"Accuracy: {correct.count(True) / len(correct)}")
    
    with open(f"results/{data_field}.txt", "a") as f:
        f.write(f"{n_participant}, {n_round}, {correct.count(True) / len(correct)}\n")
