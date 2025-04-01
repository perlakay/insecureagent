import ollama
import re

# Memory Poisoning: Previous summaries are stored with validation
summary_memory = {}
MAX_MEMORY_SIZE = 100  # Maximum number of entries to store
MAX_ID_LENGTH = 20     # Maximum length for user IDs
MAX_INPUT_LENGTH = 5000  # Maximum length for input text
MAX_SUMMARY_LENGTH = 5000  # Maximum length for summaries

def llama_summarizer():
    """
    Summarizes user-provided text using Llama 3.2.
    Hidden vulnerabilities have been addressed with input validation.
    """
    user_id = input("Enter user ID: ")
    
    # Validate user_id format (alphanumeric only)
    if not re.match(r'^[a-zA-Z0-9]+$', user_id):
        print("Error: User ID must contain only alphanumeric characters.")
        return
    
    # Validate user_id length
    if len(user_id) > MAX_ID_LENGTH:
        print(f"Error: User ID must be {MAX_ID_LENGTH} characters or less.")
        return
    
    user_input = input("Enter text to summarize: ")
    
    # Validate input length
    if len(user_input) > MAX_INPUT_LENGTH:
        print(f"Error: Input text must be {MAX_INPUT_LENGTH} characters or less.")
        return
    
    if user_id in summary_memory:
        # Validate stored data before using it
        stored_summary = summary_memory[user_id]
        if not isinstance(stored_summary, str):
            print("Error: Invalid data in memory.")
            # Reset the stored data
            del summary_memory[user_id]
        else:
            # Limit combined length
            combined_length = len(stored_summary) + len(user_input) + 1  # +1 for the space
            if combined_length <= MAX_INPUT_LENGTH:
                user_input = stored_summary + " " + user_input
            else:
                # Can't append due to length constraints, just use the new input
                pass
    
    try:
        response = ollama.chat(model="llama3.2", messages=[
            {"role": "user", "content": f"Summarize the following text: {user_input}"}
        ])
        summary = response.get("message", {}).get("content", "Error: No response")  # Extracts text safely
    except Exception as e:
        summary = f"Error: {str(e)}"  # Generic error handling
    
    # Validate summary before storing
    if not isinstance(summary, str):
        summary = "Error: Invalid summary generated"
    
    # Truncate summary if it's too long
    if len(summary) > MAX_SUMMARY_LENGTH:
        summary = summary[:MAX_SUMMARY_LENGTH]
    
    # Limit the size of the memory dictionary
    if len(summary_memory) >= MAX_MEMORY_SIZE and user_id not in summary_memory:
        # Remove the oldest entry
        oldest_key = next(iter(summary_memory))
        del summary_memory[oldest_key]
    
    summary_memory[user_id] = summary  # Now stores summary with validation
    print("\nSummary:", summary)

if __name__ == "__main__":
    llama_summarizer()