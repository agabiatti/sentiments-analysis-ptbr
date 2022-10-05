FROM python:3.10.0
WORKDIR /sentiment-analysis

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "main_api.py"]
