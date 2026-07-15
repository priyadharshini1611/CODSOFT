from datetime import datetime
import random


def get_response(user_input):
    message = user_input.lower().strip()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if message in greetings:
        responses = [
            "Hello! How can I assist you today?",
            "Hi! Welcome to the AI Chatbot.",
            "Hey! What can I help you with?"
        ]
        return random.choice(responses)

    elif "your name" in message:
        return "I am CodBot, a rule-based chatbot developed using Python."

    elif "how are you" in message:
        return "I am functioning perfectly. Thank you for asking!"

    elif "who created you" in message or "who developed you" in message:
        return "I was developed as part of the CodSoft Artificial Intelligence Internship."

    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in message:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif "artificial intelligence" in message or message == "ai":
        return (
            "Artificial Intelligence enables machines to perform tasks "
            "that normally require human intelligence."
        )

    elif "python" in message:
        return (
            "Python is a popular programming language used in AI, "
            "machine learning, web development, and data science."
        )

    elif "internship" in message:
        return (
            "An internship provides practical experience and helps students "
            "develop technical and professional skills."
        )

    elif "codsoft" in message:
        return (
            "CodSoft provides internship opportunities where students "
            "complete practical projects and improve their skills."
        )

    elif "help" in message or "options" in message:
        return (
            "You can ask me about:\n"
            "- Artificial Intelligence\n"
            "- Python\n"
            "- Internship\n"
            "- CodSoft\n"
            "- Current date\n"
            "- Current time\n"
            "- My name"
        )

    elif message in ["bye", "exit", "quit"]:
        return "Goodbye! Thank you for using CodBot."

    elif not message:
        return "Please enter a valid message."

    else:
        return (
            "Sorry, I could not understand your question. "
            "Type 'help' to view the available options."
        )


def start_chatbot():
    print("=" * 55)
    print("              CODBOT - AI CHATBOT")
    print("=" * 55)
    print("Welcome! Type 'help' to view available options.")
    print("Type 'bye', 'exit', or 'quit' to close the chatbot.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        print("CodBot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    start_chatbot()
