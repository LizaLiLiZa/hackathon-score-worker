# Написать текст к критериям
def prepare_prompt(reviews, criteria):
    prompt = "Here are some reviews about an employee:\n\n"
    for i, review in enumerate(reviews, start=1):
        prompt += f"Review {i}:\n{review['review']}\n\n"
    prompt += "take these counted grades and write near short text review about it"
    prompt += criteria
    prompt += "print criteria: grade and short review of this criteria grade. at the end general grade and general review"
    prompt += "Do not refer to specific review numbers when responding. Analyze the reviews. Please respond only in Russian.\n" 
    return prompt


# Сократить один отзыв. Учесть дату, нейтральные отзывы
def short_prompt(review):
    prompt = 'Make a short summary of the reviews. If the date of writing of the text is indicated, then the text written later has the greatest importance. \
        The short summary should characterize the person`s soft skills and be shorter than the original review. If the review already clearly characterizes the \
        person`s soft skills and does not need to be shortened, do not do this and return the same text of the review. The response contains only the text of the final review.\
        Reviews added 2 to 3 years ago have a weight of 0.3 in the final condensed review, 1 to 2 years old - 0.6, in the last year - 1. \
        If the date is not specified, consider the entire text of the review evenly.\
        If it is not possible to shorten the review correctly and additions are required from the author of the review, leave neutral feedback instead of the review.\
        If there is any obscene, inappropriate language or just bunch of symbols which do not describe scills, leave it neutral(write it in russian - нейтрально) and  do not include it to the result at all \
        If there is information which is not connected to the soft skills and not connected to work, leave it neutral and do not include it to the result\
        If there is a text not connected to the person at all, make it neutral\
        If there is a review with an information about soft skills and something not connected with them, leave info about skills and do not\
        include info about something else\
        Review:' 

    prompt+= f"{review['review']}"
    prompt+= f"ID_reviewer: {review['ID_reviewer']}, ID_under_review: {review['ID_under_review']}"

    return prompt


# Дать числовую оценку исходя из критерий и отзывов
def grade_prompt(reviews, criteria):
    prompt = 'Count the number of each criteria of a person. Use these formulas to intepretate it later.'
    prompt+= criteria
    prompt += 'k (coefficient) = (number of n-criteria)/(sum of all number of criterias)\
    if number of good criteria is more than bad: Grade = (number of good criterias - k*number of bad)/((sum of bad and good criterias)+1)*2.5 \
    if number of bad criteria is more than good: Grade = (number of good criterias*k - number of bad)/((sum of bad and good criterias)+1)*2.5 \
    if number of good = bad, make grade = 2.5\
    if there are good criterias and no bad ones, make grade = 5 \
    if there are bad criterias and no good, make grade = 2.5 - ((good - k * bad)/(bad + good + 1)*2.5) \
    overall grade = (sum of grades)/(sum of k(coefficients)) \
    do not write in which response criteria was found\
    do not include neutral at\
    example of respond: professionalism: Grade = 4.3.\
    WRITE ONLY: NAME OF CRITERIA AND ITS GRADE AND OVERALL GRADE AND DO NOT WRITE ANYTHING ELSE EVEN K (COEFFICIENT) \
    Please respond only in Russian \
        Review:' 

    for i, review in enumerate(reviews, start=1):
        prompt += f"Review {i}:\n{review['review']}\n\n"
    
    return prompt


# Дать обобщенные критерии человеку исходя из отзывов о нем.
def criteria_prompt(reviews):
    prompt = ' find soft skills criterias from review\
    do not write in which response criteria was found\
    do not include neutral reviews at\
    write grouped similar soft skills criterias in one category (make about 5 categories)\
    WRITE ONLY: NAME OF CATEGORY DO NOT WRITE ANYTHING ELSE EVEN K (COEFFICIENT) AND CRITERIAS ITSELF \
    Please respond only in Russian \
        Review:' 

    for i, review in enumerate(reviews, start=1):
        prompt += f"Review {i}:\n{review['review']}\n\n"

    return prompt

