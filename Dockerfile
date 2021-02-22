FROM python:3


COPY ["requirements.txt", "/usr/app/"]

#WORKDIR /usr/
WORKDIR /usr/app/src/

#COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r ../requirements.txt

COPY ["./src", "."]
#COPY src .
EXPOSE 5000
CMD [ "python", "blog.py" ]
#CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "wsgi:app"]
