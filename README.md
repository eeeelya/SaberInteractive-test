# SaberInteractive-test
My test project for Saber Interactive company.

## Installation
For project installation you should enter:

    git clone git@github.com:eeeelya/SaberInteractive-test.git

## Launch
    
    cd SaberInteractive-test
    sudo docker-compose up --build

## Usage 

You can access the application by this url:
    
    http://0.0.0.0:7000/

If you want to know more about API:

    http://0.0.0.0:7000/docs#/ 

## Testing 

You can send a POST request:
    
    http://0.0.0.0:7000/api/v1/get_tasks
    or 
    curl -X POST http://0.0.0.0:7000/api/v1/get_tasks -H "Content-Type: application/json" -d '{"name": <build_name>}'
