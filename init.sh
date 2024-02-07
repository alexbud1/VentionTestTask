#!/bin/bash

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('vention', 'vention@example.com', 'vention2024')" | python manage.py shell

pytest -v

# Start Django server
python manage.py runserver 0.0.0.0:8000
