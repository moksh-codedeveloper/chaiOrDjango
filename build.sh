#!/usr/bin/env bash
pip install -r requirements.txt
pip install --upgrade pip

npm install

# Build Tailwind from static_src to Django static
npx tailwindcss \
  -c theme/static_src/tailwind.config.js \
  -i theme/static_src/input.css \
  -o static/css/dist/styles.css \
  --minify

# Run Django setup
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
