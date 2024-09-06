# Используем официальный образ Python 3.9 в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt и скрипт запуска в рабочую директорию
COPY ./flask_app/requirements.txt /app/flask_app/requirements.txt
COPY ./start.sh /app/

# Устанавливаем зависимости Python из requirements.txt
RUN pip install --no-cache-dir -r /app/flask_app/requirements.txt

# Копируем остальные файлы приложения
COPY ./flask_app/ /app/flask_app/

# Даем права на исполнение скрипту start.sh
RUN chmod +x /app/start.sh

# Открываем порт 8082
EXPOSE 8082

# Запускаем скрипт start.sh при старте контейнера
CMD ["/app/start.sh"]
