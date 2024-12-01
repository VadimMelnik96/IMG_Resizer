# Resizer

Приложение для загрузки изображений по API и изменения их размера

## Запуск приложения

### Добавить .env файл со следующими параметрами:

```

STORE_UPLOADS_FOLDER=/uploads
STORE_RESIZED_FOLDER=/resized


REDIS_DSN=redis://redis:6379

APP_NAME=Image_Resizer

```

### Запустить контейнеры

```

docker-compose up -d --build

```

### Документация OpenAPI доступна по адресу: 

[Документация](127.0.0.1:8000/docs)

