# Use uma imagem base oficial do Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o diretório de trabalho
COPY . .

# Comando para rodar a aplicação usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
