def chatbot():
    print("🤖 Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello! How can I help you today?")
        
        elif 'how are you' in user_input:
            print("Bot: I'm just a bot, but I'm functioning as expected!")
        
        elif 'your name' in user_input:
            print("Bot: I am a simple chatbot created in Python.")
        
        elif 'help' in user_input:
            print("Bot: Sure! You can ask me about my name, how I am, or just say hi!")

        elif 'bye' in user_input or 'exit' in user_input:
            print("Bot: Goodbye! Have a great day! 👋")
            break

        else:
            print("Bot: I'm sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
