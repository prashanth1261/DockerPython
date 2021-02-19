FROM python:3

WORKDIR /src/app

COPY . .

RUN pip install Flask==1.0.2

CMD ["python","sample.py"]