FROM python:3.8

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000:5000
CMD [ "python3", "./src/flaskapp.py"]

