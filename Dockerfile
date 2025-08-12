FROM python:3.11-alpine

WORKDIR /python-app

# Install uv first
RUN pip install --no-cache-dir uv

# Copy dependency files first (to leverage Docker cache)
COPY pyproject.toml uv.lock ./

RUN pip install uv

RUN uv sync

# Copy the rest of the code
COPY . .

CMD ["uv", "run", "server.py"]
