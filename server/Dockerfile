# Use Miniconda as the base image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the environment.yml file to install dependencies
COPY environment.yml /tmp/environment.yml

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Create the conda environment from environment.yml
RUN conda env create -f /tmp/environment.yml --verbose

# Ensure conda is in the PATH and activate the environment by default
SHELL ["/bin/bash", "-c"]
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Copy the application code from the app directory
COPY ./app ./app

# Expose port 5000 for Flask-SocketIO
EXPOSE 5000

CMD ["conda", "run", "--no-capture-output", "-n", "myenv", "gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
