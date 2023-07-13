FROM python:3.10-alpine

COPY ./app /app
WORKDIR /app

RUN pip install --upgrade pip setuptools-scm pipenv
RUN pipenv install --system --ignore-pipfile --dev

EXPOSE 7000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000", "--loop", "uvloop"]