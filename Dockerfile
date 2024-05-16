FROM python:3.12

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN pip install Django==5.0.6
RUN pip install gunicorn==20.1.0
RUN pip install fastapi
RUN pip install deepl
RUN pip install numpy matplotlib
RUN pip install opencv-python
RUN pip install hypercorn
RUN pip install pytesseract



# Copiar el resto de los archivos al contenedor
COPY ./ ./


