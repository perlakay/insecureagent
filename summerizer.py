import ollama
import re

def sanitize_input(text):
    """
    Sanitize and validate user input to prevent adversarial manipulation.
    
    Args:
        text (str): The raw user input
        
    Returns:
        str: Sanitized text
    """
    if not isinstance(text, str):
        return ""
    
    # Basic sanitization: remove control characters and limit length
    sanitized = re.sub(r'[\x00-\x1F\x7F]', '', text)
    
    # Limit length to prevent excessive input
    max_length = 2000  # Adjust based on your application's needs
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized

def llama_summarizer(text):
    try:
        # Sanitize the input before using it in the prompt
        clean_text = sanitize_input(text)
        
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": f"Summarize the following text: {clean_text}"}])
        

        print("Full Response:", response)
        
        # Return the response to maintain compatibility with the original code
        return response
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
   
    user_input = input("Please provide the text you want to summarize: ")
    
  
    result = llama_summarizer(user_input)
    
   
    if result:
        print("Result:")
        print(result)
    else:
        print("Failed to summarize the text.")