FROM mcr.microsoft.com/azureml/curated/sklearn-0.24-ubuntu18.04-py37-cpu:33

USER root:root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    vim
