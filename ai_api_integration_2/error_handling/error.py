import requests

def make_api_call(url):
    try:
        response = requests.get(url, timeout=5) 
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.ConnectionError:
   
        return {"error": "Network error: Unable to connect to the API. Please check your internet connection."}
    
    except requests.exceptions.Timeout:

        return {"error": "Timeout error: The request took too long to complete. Please try again later."}
    
    except requests.exceptions.RequestException as e:

        return {"error": f"An error occurred: {str(e)}"}

url = "https://jsonplaceholder.typicode.com/posts"  
result = make_api_call(url)
print(result)
