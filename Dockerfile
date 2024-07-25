FROM python:3.8

WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src
COPY cert/ /cert
ENTRYPOINT ["python", "-m", "src.main"]