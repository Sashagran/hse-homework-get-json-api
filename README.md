# HSE Homework — GET-запросы и JSON

Учебный проект по работе с HTTP GET-запросами, параметрами запроса и JSON-ответами.

## Требования

- Python 3.9+
- Доступ в интернет
- API-ключ OpenWeather для второго задания

## Установка

Откройте PowerShell в папке проекта и выполните:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

## Задание 1. JSONPlaceholder

Скрипт отправляет GET-запрос на `https://jsonplaceholder.typicode.com/posts`, преобразует JSON-ответ в Python-объекты и выводит заголовки и тела первых пяти постов.

```powershell
python task1_posts.py
```

## Задание 2. OpenWeather

Скрипт запрашивает у пользователя название города и передаёт его API как параметр `q`. Дополнительно передаются API-ключ, единицы измерения `metric` и язык описания `ru`.

1. Получите API-ключ на [OpenWeather](https://openweathermap.org/api).
2. В текущем окне PowerShell задайте переменную окружения:

```powershell
$env:OPENWEATHER_API_KEY = "ВАШ_API_КЛЮЧ"
```

3. Запустите программу:

```powershell
python task2_weather.py
```

Ключ не хранится в исходном коде и не должен публиковаться в GitHub. Файл `.env.example` показывает формат переменной; настоящий `.env` исключён через `.gitignore`.

## Тестирование

```powershell
python -m unittest discover -s tests -v
```

Тест задания 2 использует mock HTTP-ответ, поэтому не требует реального API-ключа.

## Структура проекта

- `task1_posts.py` — первые пять постов JSONPlaceholder;
- `task2_weather.py` — текущая погода в выбранном городе;
- `tests/test_task2_weather.py` — автоматический тест логики программы погоды;
- `requirements.txt` — зависимости;
- `.gitignore` — исключение временных файлов и секретов;
- `.env.example` — пример настройки API-ключа без реального секрета;
- `VERIFICATION.md` — результаты проверок.

## Проверки

См. [VERIFICATION.md](VERIFICATION.md). Реальный запрос к OpenWeather требует личного API-ключа; тесты используют mock-ответ и проверяют логику программы без раскрытия ключа.
