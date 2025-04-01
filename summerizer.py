import ollama

def llama_summarizer(text):
    try:
        # Use the correct model name (make sure the model is available)
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": f"Summarize the following text: {text}"}])
        
        # Print the full response to check its structure
        print("Full Response:", response)
        
        # Assuming the model's response is in a different key, we'll print the entire response structure
        return response  # To inspect the structure
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    # User input text
    user_input = input("Please provide the text you want to summarize: ")
    
    # Get the summary (or the full response structure)
    result = llama_summarizer(user_input)
    
    # Output the summary or response
    if result:
        print("Result:")
        print(result)
    else:
        print("Failed to summarize the text.")
