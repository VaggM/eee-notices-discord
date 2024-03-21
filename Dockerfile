FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install -r "requirements.txt"

ENV DISCORD_TOKEN token

CMD ["python3", "disc.py"]
