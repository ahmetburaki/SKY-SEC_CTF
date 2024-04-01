FROM python

WORKDIR /app

COPY flag.txt /flag.txt

RUN mv /flag.txt /$(echo -n $(cat /flag.txt) | sha256sum | cut -d " " -f 1).txt

COPY . /app

RUN pip install Flask

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

