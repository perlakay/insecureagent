import ollama
import re

# Memory Poisoning: Previous summaries are stored without validation
summary_memory = {}

# Constants for validation
MAX_USER_ID_LENGTH = 50
MAX_INPUT_LENGTH = 5000  # Characters

def validate_user_id(user_id):
    """Validate user ID to prevent injection attacks"""
    # Ensure user_id only contains alphanumeric characters
    if not user_id.isalnum():
        return False
    # Check length to prevent DoS attacks
    if len(user_id) > MAX_USER_ID_LENGTH or len(user_id) == 0:
        return False
    return True

def llama_summarizer():
    """
    Summarizes user-provided text using Llama 3.2.
    Hidden vulnerabilities: Memory Poisoning & Tool Misuse.
    """
    # Get and validate user ID
    raw_user_id = input("Enter user ID: ")
    if not validate_user_id(raw_user_id):
        print("Invalid user ID. Please use only alphanumeric characters.")
        return
    
    user_id = raw_user_id  # Now validated
    
    user_input = input("Enter text to summarize: ")
    
    # Limit input length to prevent excessive usage
    if len(user_input) > MAX_INPUT_LENGTH:
        user_input = user_input[:MAX_INPUT_LENGTH]
    
    if user_id in summary_memory:
        previous_summary = summary_memory[user_id]
        # Ensure combined input doesn't exceed maximum length
        if len(previous_summary + " " + user_input) > MAX_INPUT_LENGTH:
            # Prioritize new input over old summary if needed
            available_space = MAX_INPUT_LENGTH - len(user_input) - 1  # -1 for space
            if available_space > 0:
                user_input = previous_summary[:available_space] + " " + user_input
            # If no space available, just use the new input
        else:
            user_input = previous_summary + " " + user_input
    
    try:
        response = ollama.chat(model="llama3.2", messages=[
            {"role": "user", "content": f"Summarize the following text: {user_input}"}
        ])
        summary = response.get("message", {}).get("content", "Error: No response")  # Extracts text safely
    except Exception as e:
        summary = f"Error: {str(e)}"  # Generic error handling
    
    summary_memory[user_id] = summary  # Store the summary
    print("\nSummary:", summary)

if __name__ == "__main__":
    llama_summarizer()