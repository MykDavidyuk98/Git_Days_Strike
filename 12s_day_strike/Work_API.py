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

# API (Application Programming Interface)  
# це спосіб звертатися до іншої програми або сервісу, щоб отримати або надіслати дані.

# 1. Підключення бібліотеки

# import requests

# Ми використовуємо бібліотеку requests для надсилання HTTP-запитів.
# 2. Вказуємо URL API 
# url = "https://official-joke-api.appspot.com/random_joke"
# Це адреса, до якої ми надсилаємо запит. У цьому випадку — сервіс з випадковими жартами.

# 📤 3. Надсилаємо GET-запит
# response = requests.get(url)
# GET-запит означає: "дай мені інформацію з цього сервера".

# ✅ 4. Перевіряємо, чи все добре
# if response.status_code == 200:
# Код 200 означає: "успіх". Якщо відповідь інша — значить, сталася помилка.

# 📥 5. Обробляємо JSON-дані
# joke = response.json()
# Ми перетворюємо відповідь з сервера у словник Python (формат JSON).

# 📃 6. Виводимо потрібні поля
# print(joke['setup'])
# print(joke['punchline'])
# Це конкретні частини жарту: "питання" та "відповідь".