FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt \
    && rm -rf /root/.cache

COPY . .

RUN ["python3", "nltk_downloads.py"]
RUN ["python3", "model_downloads.py"]

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]