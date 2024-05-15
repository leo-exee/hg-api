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
        f"I want a short, easy to understand, familiar description of these toilets 50 words, in the language provided. Don't mention directly cleanliness, accessibility, state. Don't mention language."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
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
        max_tokens=75,
    )

    return response.choices[0].message.content
