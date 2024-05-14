import openai
from app.models.toilet import Content


async def generate_description_service(content: Content):
    client = openai.OpenAI()

    message = (
        f"All informations :\n"
        f"Name : {content.name}\n"
        f"Address : {content.address}\n"
        f"Cleanliness : {content.cleanliness}/5\n"
        f"Accessibility : {content.accessibility}/5\n"
        f"State : {content.state}/5\n"
        f"Baby friendly : {'YES' if content.babyFriendly else 'NO'}\n"
        f"Handicap friendly : {'YES' if content.handicapFriendly else 'NO'}\n"
        f"Language : {content.language.name}\n"
        f"I want a short, relatively familiar description of these toilets in a maximum of 75 words. The text must be in the language provided in Language.The description should be familiar and friendly, as well as easy to understand. Notes should not be integrated directly into the description, but based on it."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a useful wizard that generates descriptions based on the information provided.",
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return response.choices[0].message.content
