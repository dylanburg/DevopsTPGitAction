FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD python -m unittest MyClass.py