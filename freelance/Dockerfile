FROM python:3.9
	
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
pip install --no-cache-dir -r requirements.txt

COPY . /code

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]