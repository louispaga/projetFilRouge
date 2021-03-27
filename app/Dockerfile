FROM python:3.8

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

ENV AWS_SHARED_CREDENTIALS_FILE=/app/put_yr_credentials_here/credentials
ENV AWS_PROFILE=csloginteacher
ENV AWS_PROFILE=csloginstudent

CMD [ "python3", "./src/flaskapp.py"]

