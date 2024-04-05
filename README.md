# Телеграм бот - Ссылкохранилище (@LinkVaultBot)

## Описание

Телеграм бот, который запоминает ссылки, которые ему присылают пользователи и отдает их по запросу.
Для начала взаимодействия с ботом необходимо ввести команду "/start". Далее вы увидете следующее описание функционала:

```
Привет! Я бот, который поможет не забыть прочитать статьи, найденные тобой в интернете :)

- Чтобы я запомнил статью, достаточно передать мне ссылку на нее. К примеру https://example.com
- Чтобы получить случайную статью, достаточно передать мне команду /get_article.
- Чтобы просмотреть полный список сохраненных статей, нужно воспользоваться командой /get_all_articles.

Но помни! Отдавая статью тебе на прочтение командой /get_article, она больше не хранится в моей базе.
Так что тебе точно нужно её изучить (/get_all_articles это не касается).
```

## Реализация

Бот написан при помощи библиотеки [Telebot](https://pypi.org/project/pyTelegramBotAPI/). Хранение данных происходит при помощи [SQLite](https://docs.python.org/3/library/sqlite3.html).

## Установка требуемого ПО для работы приложения

1. Необходимо установить интерпретатор [python](https://www.python.org/downloads/) версии 3.11.5 или выше;
2. Выбрать папку для скачивания приложения, скачать. Это можно сделать при помощи консольной команды: git clone url-репозитория
3. В папке с файлами приложения создать виртуальное окружение с помощью консольной команды python -m venv name, активировать его командой venv\Scripts\activate.bat для Windows или source venv/bin/activate для Linux и MacOS.
4. Установить требуемые библиотеки в активированное виртуальное окружение командой pip install -r requirements.txt
5. Для запуска приложения введите команду в консоли python main.py
