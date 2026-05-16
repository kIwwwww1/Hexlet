# Hexlet Course Project

![Демонстрация работы проекта](./preview.gif)

Full-stack веб-приложение, разработанное в рамках обучения на платформе Hexlet. Проект представляет собой интерактивную обучающую платформу с личным кабинетом, уроками и страницами тестирования.

## 🛠 Технологический стек

* **Backend:** Python, Alembic (миграции), SQLAlchemy + Asyncpg
* **Database:** PostgreSQL
* **Frontend:** Vue.js, JavaScript, CSS
* **Package Manager:** uv (современный менеджер пакетов для Python)
* **DevOps:** Docker, Docker Compose

---

## ⚙️ Настройка окружения (.env)

Перед запуском проекта необходимо создать файл `.env` строго в директории `src/backend/`.

Вы можете создать его вручную или выполнить команду из корня проекта:
```bash
touch src/backend/.env
```

Добавьте в созданный файл `src/backend/.env` следующие конфигурации для локальной работы:

```env
DB_URL=postgresql+asyncpg://user:password@db:5432/hexlet
SECRET_KEY=TeStDataFr0mLocalHost
ALGORITHM=HS256
```

---

## 🚀 Как запустить проект локально

Убедитесь, что у вас установлены [Git](https://git-scm.com) и [Docker Compose](https://docker.com).

### Вариант 1: Полный запуск через Docker (Рекомендуемый)

Самый надежный способ развернуть приложение с автоматическим применением структуры базы данных:

1. Клонируйте репозиторий и перейдите в него:
   ```bash
   git clone https://github.com
   cd Hexlet
   ```
2. Создайте файл конфигурации:
   ```bash
   touch src/backend/.env
   ```
   *(Заполните его данными из блока «Настройка окружения» выше)*
3. Соберите Docker-образы приложения:
   ```bash
   docker compose build
   ```
4. Запустите контейнер базы данных PostgreSQL в фоновом режиме:
   ```bash
   docker compose up db -d
   ```
   *(Подождите 3–5 секунд для полной инициализации СУБД)*
5. **Создание структуры таблиц для чистого проекта:**
   Выполните эту команду, чтобы синхронизировать историю Alembic, сгенерировать файлы и применить их к пустой базе данных:
   ```bash
   docker compose run --rm app sh -c "python -m alembic stamp head && python -m alembic revision --autogenerate -m 'init_tables' && python -m alembic upgrade head"
   ```
6. Запустите все остальные сервисы проекта (бэкенд и фронтенд):
   ```bash
   docker compose up -d
   ```

### Вариант 2: Смешанный запуск (БД в Docker + Backend локально)

Используйте этот вариант для разработки, чтобы вносить изменения в код бэкенда «на лету» без постоянной пересборки контейнеров:

1. Клонируйте репозиторий и перейдите в него:
   ```bash
   git clone https://github.com
   cd Hexlet
   ```
2. Создайте файл конфигурации:
   ```bash
   touch src/backend/.env
   ```
   *(Заполните его данными из блока «Настройка окружения» выше)*
3. Запустите контейнер базы данных PostgreSQL (сервис `db`) в фоновом режиме:
   ```bash
   docker compose up db -d
   ```
4. Установите зависимости Python локально с помощью `uv`:
   ```bash
   uv sync
   ```
5. Примените миграции базы данных Alembic:
   ```bash
   uv run alembic stamp head
   uv run alembic revision --autogenerate -m "init_tables"
   uv run alembic upgrade head
   ```
6. Запустите backend-сервер:
   ```bash
   uv run python src/main.py
   ```

---

## 📁 Структура проекта

* `src/` — исходный код серверной и клиентской части приложения.
* `alembic/` & `alembic.ini` — конфигурация и файлы миграций базы данных.
* `pyproject.toml` & `uv.lock` — конфигурация проекта и зафиксированные версии зависимостей.
* `docker-compose.yml` — конфигурация для одновременного развертывания приложения и СУБД PostgreSQL в Docker.
* `*.jpg` — скриншоты основных интерфейсов приложения.
