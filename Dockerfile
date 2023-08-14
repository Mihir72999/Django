FROM faucet/python3
WORKDIR /app
COPY ./requirements.txt ./
RUN  pip install -U pip && pip install -r requirements.txt
COPY . .
CMD [ "gunicorn",  "myapp.wsgi" ] 






