# VERSION 1.0.0
# AUTHOR: Ayu Peraiyantika
# DESCRIPTION: Fast API, function date with Python 3.9
# BASED ON: https://sweetcode.io/how-to-dockerize-and-deploy-a-fast-api-application-to-kubernetes-cluster/

# It instructs Docker Engine to use official python:3.9 as the base image
FROM python:3.9
LABEL maintainer="Ayu Peraiyantika"

# It creates a working directory(app/service) for the Docker image and container
RUN mkdir -p /app/
WORKDIR /app/

# Install tzdata for timezone configuration
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Optionally, set the environment variable for timezone
ENV TZ=Asia/Jakarta

# It will copy all files and the source code from the host `fast-api` folder to the `app` container working directory
COPY . .

# It will install the framework and the dependencies in the `requirements.txt` file.
RUN pip install -r requirements.txt

# It will expose the FastAPI application on port `8000` inside the container
EXPOSE 8000

# It is the command that will start and run the FastAPI application container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
