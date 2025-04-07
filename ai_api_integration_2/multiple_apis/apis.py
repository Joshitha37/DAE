import requests
import json

def get_advice():
    advice_slip_url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(advice_slip_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if "slip" in data and "advice" in data["slip"]:
            return data["slip"]["advice"]
        else:
            return {"error": "Unexpected response format from the Advice Slip API."}
    except requests.exceptions.ConnectionError:
        return {"error": "Network error: Unable to connect to the Advice Slip API. Please check your internet connection."}
    except requests.exceptions.Timeout:
        return {"error": "Timeout error: The Advice Slip API request took too long. Please try again later."}
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred with the Advice Slip API: {str(e)}"}

def get_free_activity():
    bored_api_url = "https://www.boredapi.com/api/activity?price=0.0"
    try:
        response = requests.get(bored_api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if "activity" in data:
            return data["activity"]
        else:
            return {"error": "Unexpected response format from the Bored API."}
    except requests.exceptions.ConnectionError:
        return {"error": "Network error: Unable to connect to the Bored API. Please check your internet connection."}
    except requests.exceptions.Timeout:
        return {"error": "Timeout error: The Bored API request took too long. Please try again later."}
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred with the Bored API: {str(e)}"}

if __name__ == "__main__":
    advice = get_advice()
    free_activity = get_free_activity()

    if isinstance(advice, str):
        print("Here's a piece of advice for you:")
        print(advice)
        if isinstance(free_activity, str):
            print("\nSounds like you might need something to do! Here's a free activity idea:")
            print(free_activity)
        else:
            print(f"\nCouldn't find a free activity right now. Error: {free_activity['error']}")
    else:
        print(f"Couldn't get advice right now. Error: {advice['error']}")