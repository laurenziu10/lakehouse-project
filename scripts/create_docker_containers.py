import os
import subprocess

# Docker-Container erstellen und starten
def build_and_run_container(dockerfile_path, service_name):
    # Docker-Image erstellen
    build_command = f"docker build -t {service_name} -f {dockerfile_path} ."
    subprocess.run(build_command, shell=True, check=True)
    print(f"Container built for {service_name}")
    
    # Docker-Container starten
    run_command = f"docker run -d --name {service_name} {service_name}"
    subprocess.run(run_command, shell=True, check=True)
    print(f"Container {service_name} is running.")

# Dockerfiles für die Container
dockerfiles = {
    "parquet": "docker/Dockerfile.parquet",
    "delta": "docker/Dockerfile.delta",
    "minio": "docker/Dockerfile.minio",
    "pyspark": "docker/Dockerfile.pyspark"
}

# Alle Container bauen und starten
for service, dockerfile in dockerfiles.items():
    build_and_run_container(dockerfile, service)
