import requests

response = requests.get("http://httpbin.org/status/404")    # Generates a 404 error

if response.status_code == requests.codes.not_found:
    print("Page Not Found")
else:
    print(response.status_code)


try:
    rsp = requests.get("http://httpbin.org/status/504")
    rsp.raise_for_status()                  # Raises exception if get request is not successful
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")