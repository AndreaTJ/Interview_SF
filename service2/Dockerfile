#Dockerfile for flask 
#Use Python 3.6 as a base image
FROM python:3.6
# Copy contents into image
COPY . .    
# install pip dependencies from requirements file
RUN pip3 install -r ./requirements.txt
# Expose correct port
EXPOSE 5003
# Create an entrypoint
ENTRYPOINT ["gunicorn"  , "--bind", "0.0.0.0:5003", "app:app"]
