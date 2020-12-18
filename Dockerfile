FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./opt/app/
WORKDIR ./opt/app/
RUN pip install -r requirements.txt
COPY . /opt/app/
WORKDIR ./FamilyTree