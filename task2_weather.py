"""Задание 2: получение текущей погоды в выбранном городе через OpenWeather."""

import os
import sys
import requests

# Обеспечиваем корректный ввод и вывод кириллицы в Windows-консоли.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

API_URL = "https://api.openweathermap.org/data/2.5/weather"


def main():
    city = input("Введите название города: ").strip()
    if not city:
        print("Название города не может быть пустым.")
        return

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print(
            "Не найден API-ключ OpenWeather. "
            "Сохраните ключ в переменную окружения OPENWEATHER_API_KEY "
            "и запустите программу снова."
        )
        return

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=15)
        response.raise_for_status()
        weather = response.json()

        temperature = weather["main"]["temp"]
        description = weather["weather"][0]["description"]
        city_name = weather["name"]

        print(f"Погода в городе {city_name}")
        print(f"Температура: {temperature:.1f} °C")
        print(f"Описание: {description.capitalize()}")

    except requests.exceptions.HTTPError as error:
        if response.status_code == 401:
            print("OpenWeather отклонил API-ключ. Проверьте его правильность и активацию.")
        elif response.status_code == 404:
            print("Город не найден. Проверьте название и попробуйте снова.")
        else:
            print(f"HTTP-ошибка: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении GET-запроса: {error}")
    except (ValueError, KeyError, IndexError, TypeError) as error:
        print(f"Ошибка при обработке JSON-ответа: {error}")


if __name__ == "__main__":
    main()
