def prepare_prompt(reviews):
    prompt = "Here are some reviews about an employee:\n\n"
    for i, review in enumerate(reviews, start=1):
        prompt += f"Review {i}:\n{review['review']}\n\n"

    prompt += "Based on these reviews, evaluate the employee on a scale from 1 to 5 for the following criteria:\n"
    prompt += "1. Professionalism\n2. Teamwork\n3. Communication\n4. Initiative\n5. Overall Performance\n"
    prompt += "Add short (5 sentences) explanation for each score you assigned."
    return prompt