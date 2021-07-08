
pwd
cd service2
python3 -m pytest --cov=app
cd ../service3
python3 -m pytest --cov=app
cd ../service4
python3 -m pytest --cov=app