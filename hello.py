import requests
indeed_result = requests.get("https://m.naver.com")

print(indeed_result.text)