# Simple Rule-Based Chatbot

## 📋 Overview
This is a beginner-friendly rule-based chatbot project. The chatbot uses predefined rules and responses to interact with users in a conversational manner.

## 🎯 Goal
Build a simple rule-based chatbot that can:
- Accept user input
- Match input to predefined responses using conditional logic
- Maintain conversation continuity in a loop
- Provide helpful feedback for unrecognized commands

## ✨ Features

### Supported Commands
- **"hello"** or **"hi"** → Responds with "Hi!"
- **"how are you"** → Responds with "I'm fine, thanks!"
- **"bye"** or **"goodbye"** → Responds with "Goodbye!" and exits

### Key Functionalities
- ✅ **Case-insensitive input** - Commands work regardless of capitalization
- ✅ **Whitespace handling** - Extra spaces are automatically trimmed
- ✅ **Input validation** - Alerts user if empty input is provided
- ✅ **Continuous loop** - Chatbot stays active until user says goodbye
- ✅ **User-friendly interface** - Clear prompts and formatted output

## 🛠️ Technologies Used
- **Python 3.x**
- **if-elif statements** - For input matching and conditional responses
- **Functions** - Modular code organization
- **Loops** - Continuous interaction with user
- **Input/Output** - Console-based user interaction

## 📁 Project Structure
```
codealphatask4/
├── chatbot.py      # Main chatbot application
└── README.md       # This file
```

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Execution Steps
1. Open your terminal/command prompt
2. Navigate to the project directory:
   ```bash
   cd "path\to\CodeAlpha Tasks\codealphatask4"
   ```
3. Run the chatbot:
   ```bash
   python chatbot.py
   ```

### Example Interaction
```
==================================================
Welcome to the Simple Chatbot!
Type 'hello', 'how are you', or 'bye' to chat.
==================================================

You: hello
Chatbot: Hi!

You: how are you
Chatbot: I'm fine, thanks!

You: bye
Chatbot: Goodbye!
```

## 📚 Code Structure

### `get_response(user_input)`
- **Purpose**: Processes user input and returns appropriate response
- **Parameters**: `user_input` - String containing user's message
- **Returns**: String with chatbot's response
- **Logic**: Uses if-elif-else statements to match patterns

### `run_chatbot()`
- **Purpose**: Main loop that manages chatbot interaction
- **Features**:
  - Displays welcome message
  - Continuously accepts user input
  - Calls `get_response()` to generate replies
  - Exits when chatbot says goodbye


## 📝 Learning Concepts Covered
- ✓ if-elif-else conditional statements
- ✓ Function definition and usage
- ✓ while loops for continuous execution
- ✓ User input handling
- ✓ String manipulation (lower(), strip())
- ✓ Program flow control

## 🎓 Assignment Details
**Task 4: Basic Chatbot**
- Input from user like: "hello", "how are you", "bye"
- Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!"
- Key concepts: if-elif, functions, loops, input/output

## 📄 License
This project is created for educational purposes.

---
**Happy Chatting!** 🤖
