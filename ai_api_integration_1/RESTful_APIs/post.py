import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

new_user = {
    "name": "Joshitha",
    "username": "joshitha123",
    "email": "joshitha@gmail.com"
}


response = requests.post(url, json=new_user)

new_post = response.json()

get_url = "https://jsonplaceholder.typicode.com/posts"
get_reponse = requests.get(get_url)

posts_data = get_reponse.json()
posts_data.append(new_post)

print(posts_data)