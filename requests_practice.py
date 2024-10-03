import random
import requests

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]

# Randomly choose a User-Agent from the list
headers = {'User-Agent': random.choice(user_agents)}

proxies = {
    "http": "192.73.244.36:80",
    # "https": "13.37.73.214:80"
}

params = {
    "name": "Naila",
    "age": 40
}

# Making a GET request
r = requests.get('http://httpbin.org/get', params=params, headers=headers, proxies=proxies)

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.text)

print(r.json())

# Data to be sent
payload = {
    "name": "Naila",
    "age": 40
}

# Making a POST request
r_post = requests.post('https://httpbin.org/post', data=payload)

print(r_post.json())

# To get Images
headers = {
    "Accept": "image/png"
}

r_img = requests.get("http://httpbin.org/image", headers=headers)

# Save image as file
with open("r_image.png","wb") as f:
    f.write(r_img.content)
