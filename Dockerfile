# Stage 1: Builder
FROM python:3.12-slim AS builder

# Install poetry
RUN pip install --no-cache-dir poetry==1.8.2

# Set the working directory
WORKDIR /app

# Copy the project files and install dependencies
COPY pyproject.toml poetry.lock* ./
COPY src/ ./src/

# Export dependencies and install them, then install the project
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip install --no-cache-dir --prefix="/install" -r requirements.txt && \
    poetry install --no-dev


# Stage 2: Runtime
FROM python:3.12-slim AS runtime

# Create a non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

# Add user's local bin to PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Set the working directory
WORKDIR /home/appuser/app

# Copy the installed dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy the application source code from the builder stage
COPY --from=builder /app/src/my_python_project ./my_python_project

# Set the PYTHONPATH to include the installed packages
ENV PYTHONPATH="/home/appuser/app"
