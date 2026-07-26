FROM python:3.13-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app

WORKDIR /app

RUN addgroup --system --gid 10001 telelife \
    && adduser --system --uid 10001 --ingroup telelife --home /home/telelife telelife

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY --chown=telelife:telelife . .
RUN python -m compileall -q apps packages run.py

USER telelife
CMD ["python", "run.py"]