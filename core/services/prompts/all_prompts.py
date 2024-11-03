def short_prompt(review):
    prompt = 'Make a short summary of the reviews. If the date of writing of the text is indicated, then the text written later has the greatest importance. \
        The short summary should characterize the person`s soft skills and be shorter than the original review. If the review already clearly characterizes the \
        person`s soft skills and does not need to be shortened, do not do this and return the same text of the review. The response contains only the text of the final review.\
        Reviews added 2 to 3 years ago have a weight of 0.3 in the final condensed review, 1 to 2 years old - 0.6, in the last year - 1. \
        If the date is not specified, consider the entire text of the review evenly.\
        If it is not possible to shorten the review correctly and additions are required from the author of the review, leave neutral feedback instead of the review.\
        If there is any obscene, inappropriate language or just bunch of symbols which do not describe scills, leave it neutral and  do not include it to the result at all \
        If there is information which is not connected to the soft skills and not connected to work, leave it neutral and do not include it to the result\
        If there is a text that is not related to this person at all, write: "Neutral review"\
        If there is a review with an information about soft skills and something not connected with them, leave info about skills and do not\
        Please respond in Russian\
        include info about something else\
        Review:' 

    prompt+= f"{review['review']}"
    #prompt+= f"ID_reviewer: {review['ID_reviewer']}, ID_under_review: {review['ID_under_review']}"
    return prompt

def prepare_prompt(reviews, com):
    prompt = "Here are some reviews about an employee:\n\n"
    for i, review in enumerate(reviews, start=1):
        prompt += f"Review {i}:\n{review['review']}\n\n"

    prompt += "rate the employee this review was written about on a scale of 1-5 based on the following criteria::\n"
    prompt += com
    prompt += "Do not refer to specific review numbers when responding. Analyze the reviews. Please respond in Russian."
    return prompt

