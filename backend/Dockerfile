FROM python:3.8 AS backend

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
COPY . .

EXPOSE 8000

COPY ./docker-entrypoint.sh /
ENTRYPOINT [ "bash", "/docker-entrypoint.sh" ]
CMD ["gunicorn"]
