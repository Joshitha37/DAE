import requests
import json
import os

# Gemini API URL (double-check the latest documentation for the most accurate URL)
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent"

def call_gemini_api(prompt):
    """
    Call the Gemini API with a given prompt and return the response.

    Args:
        prompt (str): The text prompt to send to the API.

    Returns:
        dict or str: The API response as a dictionary or an error message.
    """
    headers = {
        "Content-Type": "application/json",
    }
    params = {
        "key": os.environ.get("GEMINI_API_KEY")  # Get the API key from the environment variable
    }
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data, timeout=10)
        response.raise_for_status()  # Raises an exception for 4xx/5xx errors
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Network error: Unable to connect to the Gemini API. Please check your internet connection."}
    except requests.exceptions.Timeout:
        return {"error": "Timeout error: The Gemini API request took too long to complete. Please try again later."}
    except requests.exceptions.RequestException as e:
        # Include the raw response text for better debugging
        error_msg = f"Error: An error occurred with the Gemini API: {str(e)}"
        if 'response' in locals():
            error_msg += f"\nRaw response: {response.text}"
        return {"error": error_msg}

def process_response(response):
    """
    Process the API response and extract the generated text.

    Args:
        response (dict or str): The response from the API.

    Returns:
        str: The generated text or an error message.
    """
    if isinstance(response, dict) and "error" in response:
        return f"Error: {response['error']}"

    if isinstance(response, dict) and "candidates" in response and response["candidates"]:
        candidate = response["candidates"][0]
        if "content" in candidate and "parts" in candidate["content"] and candidate["content"]["parts"]:
            return candidate["content"]["parts"][0]["text"]
        else:
            return f"Unexpected response format: No content found.\nFull response: {json.dumps(response, indent=2)}"
    else:
        return f"Unexpected response format: No candidates found.\nFull response: {json.dumps(response, indent=2)}"

if __name__ == "__main__":
    # Example prompt
    user_prompt = "Write a short poem about a playful cat."

    # Call the API
    gemini_response = call_gemini_api(user_prompt)

    # Process and print the response
    result = process_response(gemini_response)
    print("Gemini's response:")
    print(result)