from openai import OpenAI

def validate_api_key(api_key):
    """Validate the OpenAI API key by making a simple request"""
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        return True
    except Exception as e:
        print(f"API key validation error: {e}")
        # Check for specific error types
        if "Incorrect API key" in str(e):
            print("The API key is incorrect or invalid")
        elif "Rate limit" in str(e):
            print("Rate limit exceeded")
        elif "Authentication" in str(e):
            print("Authentication error with the API key")
        return False 