FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade -r /app/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]






