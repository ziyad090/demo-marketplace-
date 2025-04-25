FROM python:3.11-slim

# Set work directory inside the container
WORKDIR /app

# Install uv (Rust-based fast package manager for Python)
RUN pip install uv

# Copy requirements file
COPY requirements.txt .

# Create virtual environment inside the container using uv
RUN uv venv

# Activate the virtual environment and install dependencies
RUN uv pip install -r requirements.txt

# Copy the entire source code
COPY . .
COPY .env .  

# Expose the port your MCP FastAPI app runs on
EXPOSE 9001

# Default command to run the FastAPI MCP server
CMD ["uv", "run", "okr-server.py"]
