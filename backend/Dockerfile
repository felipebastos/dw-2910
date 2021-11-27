FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

CMD [ "gunicorn", "-b", "0.0.0.0:9000", "wsgi:app" ]