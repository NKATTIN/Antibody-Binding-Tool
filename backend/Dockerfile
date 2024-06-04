FROM docker.io/library/python:3.12.1-slim-bullseye as build

# Add any system dependencies for the developer/build environment here
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    busybox \
    git \
    libmariadb-dev \
    net-tools \
    && rm -rf /var/lib/apt/lists/* \
    && busybox --install

COPY . /project
WORKDIR /project

# make the wheel outside of the venv so 'build' does not dirty requirements.txt
RUN pip install --upgrade pip build && \
    python -m build && \
    touch requirements.txt

# set up a virtual environment and put it in PATH
RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH
ENV TOX_DIRECT=1

# install the wheel and generate the requirements file
RUN pip install --upgrade pip && \
    pip install -r requirements.txt dist/*.whl && \
    mkdir -p lockfiles && \
    pip freeze  > lockfiles/requirements.txt && \
    # we don't want to include our own wheel in requirements - remove with sed
    # and replace with a comment to avoid a zero length asset upload later
    sed -i '/file:/s/^/# Requirements for /' lockfiles/requirements.txt

FROM docker.io/library/python:3.12.1-slim-bullseye as runtime

# Add apt-get system dependecies for runtime here if needed
RUN apt-get update && apt-get install -y libmariadb-dev

# copy the virtual environment from the build stage and put it in PATH
COPY --from=build /venv/ /venv/
ENV PATH=/venv/bin:$PATH


# Define the entrypoint and command to run the FastAPI application with Uvicorn
ENTRYPOINT ["uvicorn"]
CMD ["antibody-binding-api.main:app", "--host", "0.0.0.0", "--port", "8000"]