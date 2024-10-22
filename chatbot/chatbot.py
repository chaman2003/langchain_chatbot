import openai

# Set your OpenAI API key here
openai.api_key = "sk-qKbadZVVc08vA2mqFQrXYP5GetD1Gjv91Mu6wOAtiwT3BlbkFJpsLv0qSCC4Un6Xqc-71Uyq0tqUI6P9t8cluJJbpxYA"  # Replace with your actual API key

def generate_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.RateLimitError:
        return "You have exceeded your API usage limit. Please try again later."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = generate_response(user_input)
        print(f"Chatbot response: {response}")

if __name__ == "__main__":
    main()
