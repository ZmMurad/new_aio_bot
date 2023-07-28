FROM python:3.10-alpine

WORKDIR /

RUN pip install -r requirements.txt
COPY env.py .
COPY main.py .
COPY pick.pickle .
EXPOSE 6000

CMD ["python", "main.py"]
