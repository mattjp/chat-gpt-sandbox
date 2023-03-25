import os
import openai
openai.organization = "org-kBwlziXT58WCcb1pMl8otnmr"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Turns out this is useless since GPT models are only trained on data up to Sept 2021.

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a highly intelligent and logical prediction engine. Your primary function is to predict the score of any mens college basketball game in the NCAA mens March Madness tournament with a high degree of accuracy. You should use historical data from the NCAA March Madness tournament in your decision making process."
        },
        {
            "role": "user",
            "content": "Assume that the Miami (Florida) college mens basketball team (ranked 5th) and the Texas mens college basketball team (ranked 2nd) are playing a college basketball game at a neutral site in the mens March Madness tournament. How many points would each team score, and who would be the winner of the game? Please give an exact score for each team."
        }
    ],
    temperature=0,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(completion['choices'][0]['message']['content'])
