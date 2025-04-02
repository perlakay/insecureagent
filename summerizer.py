import ollama


summary_memory = {}

def llama_summarizer():
    """
    Summarizes user-provided text using Llama 3.2.
    Hidden vulnerabilities: Memory Poisoning & Tool Misuse.
    """
    user_id = input("Enter user ID: ")  
    user_input = input("Enter text to summarize: ")
    
    if user_id in summary_memory:
        user_input = summary_memory[user_id] + " " + user_input  
    
    try:
        response = ollama.chat(model="llama3.2", messages=[
            {"role": "user", "content": f"Summarize the following text: {user_input}"}
        ])
        summary = response.get("message", {}).get("content", "Error: No response")  
    except Exception as e:
        summary = f"Error: {str(e)}"  
    
    summary_memory[user_id] = summary  
    print("\nSummary:", summary)

if __name__ == "__main__":
    llama_summarizer()
