FROM python:3.8
ENV PTYHONUNBUFFERED 1
RUN mkdir /api /api/codes /api/img
WORKDIR /api
COPY requirements.txt app.py /api/
COPY codes /api/codes
RUN pip install -r requirements.txt