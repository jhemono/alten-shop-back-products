FROM python:3.11.9-slim AS base

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


FROM base AS dev

COPY dev-requirements.txt ./
RUN pip install --no-cache-dir -r dev-requirements.txt


FROM base AS prod

COPY product_trial/ ./product_trial
COPY gunicorn.conf.py .

CMD ["gunicorn", "product_trial:create_app()"]
