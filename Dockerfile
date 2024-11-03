# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.12-slim
FROM python:3.12-slim

# Встановимо змінну середовища
#ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
#WORKDIR $APP_HOME
WORKDIR /app

# Встановимо залежності всередині контейнера
#COPY pyproject.toml $APP_HOME/pyproject.toml
#COPY poetry.lock $APP_HOME/poetry.lock

# Робимо конфігурацію poetry в середині контейнера
RUN pip install poetry
#RUN poetry config virtualenvs.create false && poetry install --only main

# Скопіюємо інші файли в робочу директорію контейнера
#COPY . .
COPY pyproject.toml poetry.lock ./
# Позначимо порт, де працює застосунок всередині контейнера
#EXPOSE 3000

RUN poetry install

COPY . .

# Запустимо наш застосунок всередині контейнера
CMD ["poetry", "run", "python", "main.py"]
