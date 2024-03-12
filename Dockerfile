FROM python:3.11.5
WORKDIR /api
COPY requirements.txt /api
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /api
EXPOSE 5000