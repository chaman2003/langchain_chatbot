from chatbot.chatbot import generate_response  # Importing the generate_response function

if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = generate_response(user_input)  # Get the response from the chatbot
        print("Chatbot response:", response)
