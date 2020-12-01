FROM python:3
WORKDIR /backend_flask
ADD . ./

RUN python3 -m pip install -U pip
RUN pip3 install -r requirements.txt

CMD ["python3", "run.py"]