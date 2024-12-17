FROM python:3

WORKDIR /usr/src/app

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "hello", "run", "--host=0.0.0.0" ]
