"""Задание 1: получение первых пяти постов из JSONPlaceholder."""

import sys
import requests

# Обеспечиваем корректный вывод кириллицы в Windows-консоли.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

API_URL = "https://jsonplaceholder.typicode.com/posts"


def main():
    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        posts = response.json()

        for post in posts[:5]:
            print(f"Пост №{post['id']}")
            print(f"Заголовок: {post['title']}")
            print(f"Текст: {post['body']}")
            print("-" * 60)

    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении GET-запроса: {error}")
    except (ValueError, KeyError, TypeError) as error:
        print(f"Ошибка при обработке JSON-ответа: {error}")


if __name__ == "__main__":
    main()
