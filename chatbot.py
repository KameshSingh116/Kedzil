# Basic Chatbot Structure
# This is a simple rule-based chatbot that responds to user input

def get_response(user_input):
    """
    This function takes user input and returns a response based on predefined rules.
    """
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Basic response rules
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"

def main():
    """
    Main function to run the chatbot
    """
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get and print response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main() 