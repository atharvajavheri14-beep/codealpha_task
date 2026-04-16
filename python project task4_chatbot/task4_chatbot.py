def get_response(user_input):
    text = user_input.lower().strip()

    greetings = ["hello", "hi", "hey", "howdy", "hiya", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell", "later", "exit", "quit"]
    how_are_you = ["how are you", "how r u", "how are u", "how do you do", "whats up", "what's up"]
    thanks = ["thank you", "thanks", "thx", "thank u"]
    name_queries = ["what is your name", "who are you", "your name", "what are you"]
    help_queries = ["help", "what can you do", "commands", "options"]
    time_queries = ["what time", "current time", "tell me the time"]

    if any(word == text or text.startswith(word) for word in greetings):
        return "Hi there! Great to meet you. How can I help you today?"

    if any(phrase in text for phrase in farewells):
        return "Goodbye! It was nice chatting with you. Have a great day!"

    if any(phrase in text for phrase in how_are_you):
        return "I'm doing great, thanks for asking! I'm always ready to chat. How about you?"

    if any(phrase in text for phrase in thanks):
        return "You're welcome! Happy to help anytime."

    if any(phrase in text for phrase in name_queries):
        return "I'm PyBot, a simple Python chatbot built for the CodeAlpha internship!"

    if any(phrase in text for phrase in help_queries):
        return (
            "I can respond to:\n"
            "  - Greetings (hello, hi, hey)\n"
            "  - Farewells (bye, goodbye)\n"
            "  - How are you?\n"
            "  - What is your name?\n"
            "  - Thank you\n"
            "  - Tell me the time\n"
            "  - Tell me a joke"
        )

    if any(phrase in text for phrase in time_queries):
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    if "joke" in text:
        jokes = [
            "Why do Python programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        ]
        import random
        return random.choice(jokes)

    if "python" in text:
        return "Python is an amazing programming language! Great choice for your internship."

    if "weather" in text:
        return "I'm not connected to weather services, but I hope it's sunny where you are!"

    if "age" in text or "how old" in text:
        return "I was just created, so I'm brand new! Age is just a number anyway."

    return "I'm not sure how to respond to that. Type 'help' to see what I can do!"


def chatbot():
    print("=" * 40)
    print("       PYBOT - Simple Chatbot")
    print("=" * 40)
    print("Type 'bye' or 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("PyBot: Please say something!")
            continue

        response = get_response(user_input)
        print(f"PyBot: {response}\n")

        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    chatbot()
