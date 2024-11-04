from datasets import load_dataset

def make_mmlu_question(question, choices):
    question = question + "\n"
    for i, choice in enumerate(choices):
        question += f"({chr(ord('A')+i)}) {choice} "
    return question

def mmlu(subject):
    dataset = load_dataset("cais/mmlu", subject)["test"]

    # yield len(dataset)
    yield 100
    
    for i, data in enumerate(dataset):
        # 시간 관계상 100개만 사용
        if i == 100:
            break
        question = make_mmlu_question(data["question"], data["choices"])
        ground_truth = chr(ord('A') + data["answer"] - 1)
        yield question, ground_truth