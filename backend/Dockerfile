FROM python:3.9-slim

# Создаем пользователя
RUN addgroup --system appuser && \
    adduser --system --group appuser

WORKDIR /app

COPY app.py .

# Меняем владельца файлов
RUN chown -R appuser:appuser /app

# Переключаемся на обычного пользователя
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]