import ollama

def llama_summarizer(text):
    try:
        
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": f"Summarize the following text: {text}"}])
        

        print("Full Response:", response)
        
        
        
    except Exception as e:
        print("An error occurred during summarization.")
        return None

if __name__ == "__main__":
   
    user_input = input("Please provide the text you want to summarize: ")
    
  
    result = llama_summarizer(user_input)
    
   
    if result:
        print("Result:")
        print(result)
    else:
        print("Failed to summarize the text.")