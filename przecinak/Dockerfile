FROM python:3.10-slim AS poetry-dump

RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/
ENV PATH="${PATH}:/root/.poetry/bin"
COPY pyproject.toml .
RUN poetry export -o requirements.txt

FROM python:3.10-slim

WORKDIR /app
COPY --from=poetry-dump requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ /app/
EXPOSE 80
ENV DB_URL=/sqlitedata/db.sqlite3
VOLUME /sqlitedata/
CMD uvicorn przecinak.api:app --host 0.0.0.0 --port 80


