FROM python

WORKDIR /myapp

COPY ./sql_demo.py .

RUN pip install pymysql

EXPOSE 3306

CMD [ "python", "sql_demo.py" ]


