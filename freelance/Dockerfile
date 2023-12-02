FROM python:3.10

WORKDIR /freelance

COPY requirements.txt requirements.txt

COPY . .

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "manage.py", "runserver"]
