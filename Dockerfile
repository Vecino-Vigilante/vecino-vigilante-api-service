FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY /app /app

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app"]