# Learning Log («Журнал обучения»)

Веб-приложение на Django для ведения заметок по изучаемым темам с поддержкой учётных записей пользователей и адаптивным интерфейсом Bootstrap.

## Запуск проекта на новом компьютере (например, в колледже)

### 1. Клонирование репозитория
```bash
git clone <ВАША_ССЫЛКА_НА_РЕПОЗИТОРИЙ>
cd learning_log
```

### 2. Создание и активация виртуального окружения
- **Windows (PowerShell/cmd):**
  ```bash
  python -m venv ll_env
  ll_env\Scripts\activate
  ```
- **Linux / macOS:**
  ```bash
  python3 -m venv ll_env
  source ll_env/bin/activate
  ```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Применение миграций базы данных
```bash
python manage.py migrate
```

### 5. Создание суперпользователя (администратора)
*(опционально, если нужно заходить в админку)*
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера разработки
```bash
python manage.py runserver
```
Приложение будет доступно по адресу: **http://127.0.0.1:8000/** (или http://localhost:8000/).
