FROM python:3.12-slim                
WORKDIR /app                         
COPY sensor.py .                     
ENV BACKEND_URL=http://backend:8000  
CMD ["python", "sensor.py"]         