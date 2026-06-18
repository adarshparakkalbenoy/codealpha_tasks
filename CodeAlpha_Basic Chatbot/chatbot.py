"""
Simple Rule-Based Chatbot
Task 4: Basic Chatbot for CodeAlpha
"""

def get_response(user_input):
    """
    Function to get predefined replies based on user input.
    
    Args:
        user_input: String containing user's input
        
    Returns:
        A string with the chatbot's response
    """
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Use if-elif statements to match user input to predefined replies
    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand. Please try: hello, how are you, or bye."


def run_chatbot():
    """
    Main function to run the chatbot.
    Uses a loop to keep the chatbot running until user says goodbye.
    """
    print("=" * 50)
    print("Welcome to the Simple Chatbot!")
    print("Type 'hello', 'how are you', or 'bye' to chat.")
    print("=" * 50)
    print()
    
    # Loop to keep chatbot running
    while True:
        # Get input from user
        user_input = input("You: ").strip()
        
        # Check if input is empty
        if not user_input:
            print("Please enter something!")
            continue
        
        # Get response from chatbot
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        print()
        
        # Exit if user says goodbye
        if user_input.lower() in ["bye", "goodbye"]:
            break


# Main program execution
if __name__ == "__main__":
    run_chatbot()
