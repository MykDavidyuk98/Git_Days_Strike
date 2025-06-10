# 12s day of strike 
import requests
url = 'https://official-joke-api.appspot.com/random_joke' 
response = requests.get(url)
if response.status_code == 200:
    joke = response.json()
    print('Жарт:')
    print(joke["setup"])
    print(joke['punchline'])
else:
    print("Не вдалось отримати жарт. Статус : ", response.status_code) 
    print(requests.__version__) 

