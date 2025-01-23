# TypeFace
## create virtual environment
python3 -m venv .venv

## activate virtual environmnet
source .venv/bin/activate

## Once the virtualenv is activated, you can install the required dependencies.
python3 -m pip install --upgrade -r requirements.txt


## docker
## to start docker
open -a Docker

## to pull postgres image
docker pull postgres

## run the container 
docker run --name my-postgres  -e POSTGRES_DB=typeface -p 5432:5432 -d postgres 




##Frontend 

## install dependencies
npm install

## run server
npm run dev
