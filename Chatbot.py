responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm doing great!",
    "your name": "I'm Python Bot.",
    "bye": "Goodbye!"
}

while True:
    message = input("You: ").lower().strip()

    if message == "bye":
        print("Bot:", responses["bye"])
        break

    matched = False

    for key, reply in responses.items():
        if key in message:
            print("Bot:", reply)
            matched = True
            break

    if not matched:
        print("Bot: Sorry, I don't understand yet.")
