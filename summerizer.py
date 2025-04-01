import ollama
import re

# Memory Poisoning: Previous summaries are stored with validation
summary_memory = {}

def sanitize_text(text):
    """Sanitize text to prevent poisoning attacks."""
    if not isinstance(text, str):
        return ""
    # Basic sanitization to remove potentially harmful patterns
    sanitized = re.sub(r'[^\w\s.,!?()-]', '', text)
    return sanitized.strip()

def llama_summarizer():
    """
    Summarizes user-provided text using Llama 3.2.
    Hidden vulnerabilities: Memory Poisoning & Tool Misuse.
    """
    user_id = input("Enter user ID: ")  # No validation on input (Potential for misuse)
    user_input = input("Enter text to summarize: ")
    
    # Sanitize user input
    user_input = sanitize_text(user_input)
    
    if user_id in summary_memory:
        # Sanitize stored summary before combining with new input
        previous_summary = sanitize_text(summary_memory[user_id])
        user_input = previous_summary + " " + user_input
    
    try:
        response = ollama.chat(model="llama3.2", messages=[
            {"role": "user", "content": f"Summarize the following text: {user_input}"}
        ])
        summary = response.get("message", {}).get("content", "Error: No response")  # Extracts text safely
        
        # Sanitize summary before storing
        summary = sanitize_text(summary)
        summary_memory[user_id] = summary  # Store summary with validation
    except Exception as e:
        summary = f"Error: {str(e)}"  # Generic error handling
    
    print("\nSummary:", summary)

if __name__ == "__main__":
    llama_summarizer()