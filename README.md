# Antibody Analysis FastAPI

This repository contains a FastAPI backend for analysing antibody binding data. The application processes uploaded CSV files containing antibody binding data by calculating statistical measures (minimum, maximum, and mean optical densities) for each amino acid sequence and generating a histogram of the optical densities. Users can upload their CSV files via an endpoint, and the application returns paths to the generated statistics and histogram files, which can then be downloaded via another endpoint.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip
- Docker
- Ansible (for deployment)

### Run Development Environment

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nkattin/antibody-binding-tool.git
   cd antibody-binding-tool/backend
   ```

2. **Create virtual env**

   ```bash
    python -m venv venv
    source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
    cd backend
    pip install .
   ```

2. **Running application**

   ```bash
    cd src
    uvicorn antibody_binding_api.main:app --reload --host 0.0.0.0 --port 8000
   ```

    The application will be available at http://localhost:8000/api/docs.


3. **Using application**

    Once the application is running, you can use the following endpoints:

    1. Upload a CSV file:

        ```bash
        curl -X POST "http://localhost:8000/api/upload/" -F "file=@path_to_your_file.csv"
        ```
    
    2. Download the generated histogram or statistics CSV:

        ```bash
        curl -O "http://localhost:8000/api/download/filename.csv"
        ```

        The filename will likely be generated as histogram.png or stats.csv.


### Running Tests

    To run tests using Pytest, follow these steps:

   ```bash
    cd backend
    pytest
   ```


## Deployment

This project uses Ansible for deployment. The deployment files are untested and can be found on the feature/add-ansible-deployment branch. 

### Deployment steps

1. **Set up inventory file (hosts.ini)**

    Replace the below with your server IP and and also your SSH user.

    ```bash
    [servers]
    server_ip ansible_user=your_ssh_user
   ```

2. **Configure secrets in Github**

    1. `DOCKER_USERNAME`: Docker Hub username
    2. `DOCKER_PASSWORD`: Docker Hub password
    3. `SSH_PRIVATE_KEY`: Private ssh key for accessing production server
    4. `SSH_USER`: Username for access to production server

3. **Run ansible playbook**

    This should be handled automatically through Github workflows. To run it manually, run the below:

    ```bash
    ansible-playbook -i deploy/hosts.ini deploy/deploy.yml --private-key /path/to/private_key -u your_ssh_user
   ```





