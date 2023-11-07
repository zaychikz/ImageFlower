FROM python:3.9
WORKDIR /ImageFlower
COPY ./requirements.txt /ImageFlower/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /ImageFlower/requirements.txt

COPY ./app /ImageFlower/app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

ENV PYTHONPATH="${PYTHONPATH}:/ImageFlower"

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]