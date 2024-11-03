from input_data import load_reviews

from promts import prepare_prompt

from model import evaluate_reviews_with_llm

file_path = "./all/sample_reviews.json"
reviews = load_reviews(file_path)

promt_1 = prepare_prompt(reviews)

print(evaluate_reviews_with_llm(promt_1))