#Задача №2
import requests #Используется для запросов из интернета
from faker import Faker #Используется для генерации искуственных пользователей

def show_my_ip():
    url = "https://api.ipify.org"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"Ваш публичный IP-адрес: {response.text}")
        else:
            print(f"Сервер ответил с ошибкой: {response.status_code}")

    except requests.exceptions.RequestException:
        print("Не удалось подключиться к интернету.")


if __name__ == "__main__":
    show_my_ip()
print("\n")
fake = Faker("en_GB")
print("Генерация случайного пользователя:")
print(f"Имя: {fake.name()}")
print(f"Адрес: {fake.address()}")

#Задача №2
def two_numbers(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]



nums = [2, 7, 11, 15]
target = 26

result = two_numbers(nums, target)

print(result)

