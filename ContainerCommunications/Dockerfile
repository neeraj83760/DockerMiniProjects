FROM python

WORKDIR /myapp

COPY ./api_demo.py .

RUN pip install requests         # container ke andar api request karne ke liye ek package install karna padega

CMD [ "python", "api_demo.py" ]
