FROM python:3.11-alpine
WORKDIR /mini-app-mysql

COPY ./.env /mini-app-mysql/.env
COPY ./requirements.txt /mini-app-mysql/requirements.txt
RUN pip install -r /mini-app-mysql/requirements.txt

COPY ./app /mini-app-mysql/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]