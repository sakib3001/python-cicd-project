FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY src /app/src
EXPOSE 5000
ENV FLASK_ENV=production
CMD ["python", "src/webee/app.py"]
