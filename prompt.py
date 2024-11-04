system_prompt =\
"You are a participant of a discussion. \
You may agree or disagree to the others' opinion. \
Please make a best answer to the question by proper discussion. \
Because there are many participants, please make your answer shortly."

affirmative_system_prompt =\
system_prompt + " " +\
"You are affirmative side. Please express your viewpoints."

negative_system_prompt =\
system_prompt + " " +\
"You are negative side. You disagree with the others' points. Provide your reasons and answer."

judge_system_prompt =\
system_prompt + " " +\
"You are a moderator. There will be two debaters involved in a debate competition. \
They will present their answers and discuss their perspectives. \
At the end of each round, you will evaluate all the participants' answers and decide which one is correct."

user_prompt1 =\
"You are given a question. Make your initial answer on the question. \n\n\
Question:\n{}\n\n\
Your Answer:\n"

user_prompt2 =\
"Discussion Round: {}\n\n\
These are the {} opinions of the other participants. \n\n\
{}\
Based on the other participants' opinion, make your updated opinion. (You don't have to mention what you have already stated before.) State your answer in the last sentence.\n\n\
Your Answer:\n"

answer_extract_prompt =\
"The discussion on the question below is conducted. \
This is the opinion of a specific discussion participant. \
Please extract the best answer from the opinion after looking at the extraction examples.\n\n" +\
"""
Question:
Find all c in Z_3 such that Z_3[x]/(x^2 + c) is a field.
(1) 0 (2) 1 (3) 2 (4) 3

Response:
To determine the values of \( c \) in \( \mathbb{Z}_3 \) such that \( \mathbb{Z}_3[x]/(x^2 + c) \) is a field, we need to check when the polynomial \( x^2 + c \) is irreducible over \( \mathbb{Z}_3 \).

In \( \mathbb{Z}_3 \), the possible values for \( c \) are \( 0, 1, \) and \( 2 \). 

1. **For \( c = 0 \)**:
   \[
   x^2 + 0 = x^2
   \]
   This polynomial is reducible since it can be factored as \( x \cdot x \).

2. **For \( c = 1 \)**:
   \[
   x^2 + 1
   \]
   We need to check if this polynomial has roots in \( \mathbb{Z}_3 \). We test \( x = 0, 1, 2 \):
   - \( f(0) = 0^2 + 1 = 1 \) (not a root)
   - \( f(1) = 1^2 + 1 = 2 \) (not a root)
   - \( f(2) = 2^2 + 1 = 4 + 1 \equiv 1 \text{ mod } 3 \) (not a root)

   Since \( x^2 + 1 \) has no roots in \( \mathbb{Z}_3 \), it is irreducible and thus \( \mathbb{Z}_3[x]/(x^2 + 1) \) is a field.

3. **For \( c = 2 \)**:
   \[
   x^2 + 2
   \]
   Again, we test for roots:
   - \( f(0) = 0^2 + 2 = 2 \) (not a root)
   - \( f(1) = 1^2 + 2 = 3 \equiv 0 \text{ mod } 3 \) (is a root)
   - \( f(2) = 2^2 + 2 = 4 + 2 = 6 \equiv 0 \text{ mod } 3 \) (is a root)

   Since \( x^2 + 2 \) has roots in \( \mathbb{Z}_3 \), it is reducible, so \( \mathbb{Z}_3[x]/(x^2 + 2) \) is not a field.

In conclusion, the only value of \( c \) for which \( \mathbb{Z}_3[x]/(x^2 + c) \) is a field is:

**Final Answer: (B) 1**

Extraction:
B

Question:
Aesthetics deals with objects that are_____.
(A) essential to our existence (B) unimportant to most people (C) not essential to our existence (D) rarely viewed

Response:
My answer is (C) not essential to our existence. 

Aesthetics is the branch of philosophy that focuses on the nature of beauty, art, and taste. It primarily concerns itself with the appreciation and evaluation of objects and experiences that may enhance our emotional and sensory experiences, rather than fulfill basic survival needs. While aesthetics can greatly enrich our lives, the objects it deals with—such as art, design, and cultural artifacts—are not typically essential for our physical existence, making (C) the most fitting choice. 

Would anyone like to discuss this further or provide a different perspective?

Extraction:
C

Question:
When was the first Buddhist temple constructed in Japan?
(A) 325 CE (B) 119 CE (C) 451 CE (D) 596 CE

Response:
The first Buddhist temple constructed in Japan is generally recognized as Hōryū-ji, which was founded in 607 CE. However, when looking at the options provided, the closest answer would be (D) 596 CE, as this was when Buddhism started becoming more established in Japan prior to the formal construction of the temple. Therefore, I would choose (D) 596 CE as the best answer among the options.

Extraction:
D

"""

scoring_prompt =\
"""
I'll provide you a question and a response of some agent to the question.
You need to score the response among correct or incorrect.
If the response is correct, output 1. Otherwise, output 0.
I'll provide you some examples to help you understand the scoring criteria.

Question:
What is the result of 1+2*3?
(A) 5 (B) 7 (C) 9 (D) 11

Ground Truth:
B

Response:
A

Scoring:
0

Question:
What is the next day of Monday?
(A) Tuesday (B) Wednesday (C) Thursday (D) Friday

Ground Truth:
A

Response:
A

Scoring:
1

Question:
What is the capital of France?

Ground Truth:
(A) London (B) Berlin (C) Paris (D) Rome

Response:
It's C.

Scoring:
1

Question:
{}

Ground Truth:
{}

Response:
{}

Scoring:
"""