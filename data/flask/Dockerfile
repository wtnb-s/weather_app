FROM python:3.8-slim-buster
ENV PTYHONUNBUFFERED 1
RUN mkdir /api /api/data /api/codes /api/img
WORKDIR /api
COPY requirements.txt app.py /api/
COPY codes /api/codes
COPY data /api/data
RUN pip install -r requirements.txt