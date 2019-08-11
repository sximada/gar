FROM python:3.8.0b3-alpine3.10
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry install
CMD poetry run python -m service_pingpong
