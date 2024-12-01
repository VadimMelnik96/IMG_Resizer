FROM python:3.12.2-slim

# Set the working directory in the container to /app
WORKDIR /app

ARG POETRY_PARAMS="--without dev"
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS=ignore
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=/app/src

# Install recommended and necessary system dependencies
RUN apt-get update -y --no-install-recommends && \
    apt-get install -y --no-install-recommends \
    git gcc && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies from requirements.lock
COPY requirements.lock /app/
RUN sed '/-e/d' requirements.lock > requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose the port the webapp will run on
EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
