FROM python:3.11

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN python -m unittest discover -s tests -p 'test_*.py'

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]