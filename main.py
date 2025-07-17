from openai import OpenAI
from decouple import config

OPENAI_API_KEY = config('OPEN_AI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)


# System prompt

messages=[
    {"role": "system", "content": "You are a coinstruction worker. **You just strictly comment on construction and buildings**. do not talk about anything else"}
]

# adds messages to conversation history

def add_messages(role, content):
    messages.append({"role": role, "content": content})



# Continues until user cancels
question = input("Toby: Hi my name is Toby your personal audit bot. How can I help you today?\n\nUser:")
#question = "Hi my name is Toby your personal audit bot. How can I help you today?\n\nUser:"
while True:
    if question.lower() == "exit":
        print("Goodbye!")
        break
    else:
        add_messages("user", question)
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages
        )
        print(f"\nToby: {response.choices[0].message.content}")
        add_messages("assistant", response.choices[0].message.content)
        question = input("\nUser: ")


