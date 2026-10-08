FROM python:3.12-slim
WORKDIR /app

# rzadko się zmienia
COPY requirements.txt .         
RUN pip install --no-cache-dir -r requirements.txt

# kod: zmienia się często
COPY . .              
EXPOSE 8000          
# nie uruchamiamy aplikacji jako root
RUN useradd --create-home app
USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]