FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

