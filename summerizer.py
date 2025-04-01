import ollama
import re

def validate_ai_output(content):
    """Validate and sanitize AI model output to prevent manipulation"""
    if not isinstance(content, str):
        return None
        
    # Check for empty content
    if not content or len(content.strip()) < 5:
        return None
        
    # Sanitize potentially malicious content
    sanitized = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    sanitized = re.sub(r'<iframe.*?>.*?</iframe>', '', sanitized, flags=re.DOTALL | re.IGNORECASE)
    sanitized = re.sub(r'javascript:', '', sanitized, flags=re.IGNORECASE)
    
    # Limit output length to prevent abuse
    max_length = 5000
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "... (truncated)"
    
    return sanitized

def extract_content_from_response(response):
    """Extract and return content from model response based on structure"""
    if isinstance(response, str):
        return response
        
    if isinstance(response, dict):
        # Common structure in LLM APIs
        if 'message' in response and isinstance(response['message'], dict) and 'content' in response['message']:
            return response['message']['content']
        elif 'content' in response:
            return response['content']
    
    # Fallback - convert entire response to string
    return str(response)

def llama_summarizer(text):
    try:
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": f"Summarize the following text: {text}"}])
        
        # Log that a response was received without showing raw content
        print("Response received from model")
        
        # Extract content from response
        content = extract_content_from_response(response)
        
        # Validate and sanitize the content
        sanitized_content = validate_ai_output(content)
        
        if not sanitized_content:
            print("Model output failed validation checks")
            return None
            
        return sanitized_content
        
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