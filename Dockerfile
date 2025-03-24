FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip --no-cache-dir

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root


COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]