
import re

rules = {
    r'hello|hi|hey': 'Hi there! How can I help you today?',
    r'how are you|how\'s it going': 'I\'m just a bunch of code, but I\'m doing great, thanks for asking!',
    r'what is your name|who are you': 'I\'m GrokBot, your friendly rule-based assistant!',
    r'bye|goodbye|see you': 'Catch you later! Have a great day!',
    r'help|support|assist': 'I\'m here to answer your questions. Try asking about the weather, time, or just say hi!',
    r'weather|forecast': 'I don\'t have real-time data, but I can suggest checking a weather app or asking about something else!',
    r'time|what time is it': 'I don\'t have a clock, but you can check the time on your device!',
    r'thank you|thanks': 'You\'re welcome!',
    r'.*': 'Hmm, not sure how to respond to that. Try saying "hello", "help", or "bye"!'  # Default response
}

def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Check each rule for a match
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return rules[r'.*']  # Fallback to default response

def main():
    print("Welcome to HamsiniBot! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ['bye', 'goodbye', 'see you']:
            print("HamsiniBot: Catch you later! Have a great day!")
            break
        
        # Get and print response
        response = get_response(user_input)
        print(f"HamsiniBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()
