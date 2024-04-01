FROM python:3.7


    
COPY . /code

EXPOSE 5361
WORKDIR /code
RUN pip install --no-cache-dir -r eshop/requiriments.txt

RUN python eshop/manage.py collectstatic

ENTRYPOINT [ "python" ,"eshop/manage.py"]
CMD ["runserver","0.0.0.0:5361"]