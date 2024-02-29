FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

USER root

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY app.py /app/

EXPOSE 8105

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8105"]