FROM python:3-alpine
WORKDIR /service
COPY requirements.txt .
ARG pip_extra_args=""
RUN pip install ${pip_extra_args} --no-cache-dir -r requirements.txt
COPY . ./
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]
