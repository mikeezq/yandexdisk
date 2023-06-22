Запуск контейнера с postgres: ./run_postgres.sh
Создание миграции: file_manager-db revision --message=<your message> --autogenerate
Применение миграции к базе: file_manager-db upgrade head