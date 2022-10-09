# Развертывание на локальной машине
1. Создаем виртуальное окружение: python3 -m venv flask_venv
1. Активируем venv: source flask_venv/bin/activate
1. Устанавливаем зависимости: pip install -r requirements.txt
1. Создаем локальную БД: flask db upgrade

# Миграции
1. Активировать миграции: flask db init
2. Создать миграцию: flask db migrate -m "comment"
3. Применить миграции: flask db upgrade

# Ссылки
все ссылки (гист):
https://gist.github.com/boo-learn/738d481539239bc8408f30bab9d8312d



Дублирую содержание гиста сюда:

- ОСНОВНЫЕ МАТЕРИАЛЫ
1. Теория и Задания(Гугло-диск):
https://drive.google.com/drive/folders/1d61I6sB-UeQX0SPihrzLDiyvirGE24-2?usp=sharing
2. Операции с тегами в терминале:
https://pastebin.com/YkMRJeQ3

- ПРОЕКТЫ КУРСА
1. Проект: QuoteApi:
https://github.com/boo-learn/QuoteAPi_11_09.git
2. Проект: NoteApi:
https://github.com/boo-learn/NoteAPi_11_09.git

- ДОПОЛНИТЕЛЬНЫЕ МАТЕРИАЛЫ
1. Телеграм группа для обсуждения(временная): https://t.me/+eYedLFVG5dszMjYy
2. Виртуальные машины: https://drive.google.com/drive/folders/1AFK38cpP5d1FVAKcJVnx2AZDqqcDw5g4?usp=sharing
3. API examples:
- GitHub API: https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps
- YahooFinance: https://www.yahoofinanceapi.com/
- PetStore: https://petstore.swagger.io/
4. Из телеграм-чата:
Обещанное видео: https://youtu.be/UfeZ-bPFs10
Оно про go, но вполне универсально ("Безопасность в Golang")


почта преподавателя: eyurchenko@specialist.ru
