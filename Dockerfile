# Stage 1: Builder
FROM python:3.12-slim AS builder

# Install Poetry
RUN pip install --no-cache-dir poetry==1.8.2

# Set the working directory
WORKDIR /app

# Copy the project files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Stage 2: Runtime
FROM python:3.12-slim AS runtime

# Create a non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

# Add user's local bin to PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Set the working directory
WORKDIR /home/appuser/app

# Copy the requirements file from the builder stage
COPY --from=builder /app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the application code
COPY src/ ./src/
