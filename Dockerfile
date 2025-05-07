# Dockerfile

# Use a imagem oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos para o container
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o container
COPY . .

# Execute o bot
CMD ["python", "bot.py"]