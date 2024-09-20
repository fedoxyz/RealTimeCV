FROM continuumio/miniconda

# Create and activate the environment
RUN conda create -n myenv python=3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements file
COPY requirements.txt .

# Activate the environment and install dependencies
RUN /bin/bash -c "source activate myenv && pip install -r requirements.txt"

# Copy the application code
COPY ./app ./app

EXPOSE 8000

# Command to run the FastAPI application
CMD ["conda", "run", "-n", "myenv", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
