# Utilizziamo una immagine base di Python
FROM python:3.9-slim

# Impostiamo la directory di lavoro
WORKDIR /app

# Copiamo il file requirements.txt e installiamo le dipendenze
COPY src/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamo il resto del codice dell'applicazione
COPY . /app/

# Esponiamo la porta su cui Django serve l'applicazione
EXPOSE 8000

# Definiamo il comando di avvio
CMD ["gunicorn", "keazy_server.wsgi:application", "--bind", "0.0.0.0:8000"]
