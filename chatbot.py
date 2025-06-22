def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

print("🤖 ChatBot: Hello! You can talk to me. Type 'bye' to exit.\n")

while True:
    user_input = input("👤 You: ")
    response = chatbot_response(user_input)
    print("🤖 ChatBot:", response)

    if user_input.lower() == "bye":
        break
