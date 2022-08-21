import requests
indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&vjk=22cfba9a17148053")

print(indeed_result)