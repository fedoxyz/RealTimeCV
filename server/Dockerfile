FROM continuumio/miniconda

WORKDIR /usr/src/app

# Copy the environment.yml file
COPY environment.yml /tmp/environment.yml

# Install dependencies
RUN conda env create -f /tmp/environment.yml

# Ensure conda is in the PATH and make environment active by default
SHELL ["/bin/bash", "-c"]
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Copy the application code
COPY ./app ./app

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["conda", "run", "-n", "myenv", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

