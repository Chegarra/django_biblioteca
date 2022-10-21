# Primero, seleccionamos version completa de python para compilar todo lo necesario en requirements
FROM python:3.8-buster AS builder

COPY ./requirements.txt ./requirements.txt
RUN pip install --user -r requirements.txt

# Segundo, seleccionamos version slim
FROM python:3.8-slim-buster

# Tercero, copiamos solo la instalacion de las dependencias  de la primera imagen de python
COPY --from=builder /root/.local /root/.local

# Cuarto, copiamos el código fuente
COPY ./biblioteca/ /biblioteca
WORKDIR /biblioteca

# Quinto, añadir variables de entorno de python
ENV PYTHONPATH /
ENV PATH=/root/.local/bin:$PATH