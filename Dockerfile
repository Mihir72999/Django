FROM faucet/python3
WORKDIR /app
COPY ./requirements.txt ./
RUN  pip install -U pip && pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD [ "python3",  "manage.py" , "runserver" ] 






