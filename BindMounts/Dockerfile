FROM python

WORKDIR /myapp

COPY  ./myapp.py .   # COPY . . ka matlab bindmount folder me jitni bhi files hai sab container ka part banegi

COPY ./servers.txt .

CMD [ "python", "myapp.py" ]
