FROM continuumio/miniconda3

WORKDIR /usr/src/app

COPY environment.yml /tmp/environment.yml

RUN conda env create -f /tmp/environment.yml

SHELL ["/bin/bash", "-c"]
ENV PATH /opt/conda/envs/myenv/bin:$PATH

COPY ./app ./app

EXPOSE 5000

CMD ["conda", "run", "-n", "myenv", "python", "app/app.py"]

