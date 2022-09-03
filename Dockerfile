FROM ubuntu:22.10

LABEL maintainer="luistavares10@outlook.pt"
LABEL description="ARM64 and RISC-V (extensible) assessment system"
LABEL version="0.1.0"

SHELL ["/bin/bash", "-c"]

WORKDIR /usr/app

# Dependencies directory (system wide and Python py_requirements.txt)
COPY requirements /requirements

# Tool source code
COPY ./ /usr/app

# Ensure packages are up to date
RUN apt-get update

# Install
RUN sh /requirements/system_requirements.sh

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${PATH}:/root/.local/share/pypoetry/venv/bin"

RUN poetry install

RUN echo 'alias areas="python3 /areas/main.py"' >> ~/.bashrc

# Default command
CMD ["/bin/bash"]
