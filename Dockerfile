# Use a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Atualiza o pip
RUN pip install --upgrade pip

# Copia o arquivo de dependências para o diretório atual do container
COPY requirements.txt /app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código fonte do projeto para o container
COPY . /app

# Coleta os arquivos estáticos (necessário para a execução de certos projetos Django)
#RUN python manage.py collectstatic --noinput

# Expõe a porta 8000 para acesso externo ao container
EXPOSE 8000

# Define o comando para iniciar a aplicação
CMD ["gunicorn", "casepro.wsgi:application", "--bind", "0.0.0.0:8000"]
