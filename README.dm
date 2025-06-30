```markdown
# Reference Manager

Удобный бэкенд на Django + динамический фронтенд на Bootstrap для управления справочниками:
- **Фабрика** → **Участки** → **Оборудование**
- CRUD через DRF API и обновляемый без перезагрузки HTML-интерфейс
- Динамические таблицы с сортировкой, нумерацией и бейджами

---

## Функциональные возможности

- Создание / редактирование / удаление фабрик, участков и оборудования
- Для каждого оборудования отображаются связанные участки и фабрики
- Динамическое добавление записей без перезагрузки страницы (AJAX + Fetch)
- Таблицы с порядковым номером, сортировкой по фабрикам и участкам
- Интерактивные Bootstrap-карточки и таблицы

---

## Технологии

- Python 3.8+
- Django 4.x
- Django REST Framework
- SQLite (по умолчанию) или PostgreSQL
- Bootstrap 5
- Vanilla JavaScript (Fetch API)

---

## Установка

```bash
# 1. Клонировать
https://github.com/AntonSergeevich/backend-factory.git
cd reference-manager

# 2. Войти в виртуальное окружение
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py migrate

# 5. Запустить сервер
python manage.py runserver
```

Откройте в браузере:
- API-документацию DRF → `http://localhost:8000/api/`
- HTML-интерфейс → `http://localhost:8000/`
- Админ-панель → `http://localhost:8000/admin/`
- Логин/пароль → 'admin/admin'

---

## Структура проекта

```
reference-manager/
├── core/
│   ├── migrations/         # миграции моделей
│   ├── templates/core/     # HTML-шаблоны
│   │   ├── base.html
│   │   ├── index.html
│   │   └── hierarchy.html
│   ├── models.py           # Factory, Unit, Equipment
│   ├── serializers.py      # DRF сериализаторы
│   ├── views.py            # ViewSets + HTML-views
│   ├── utils.py            # рекурсивный поиск родителей/детей
│   ├── urls.py             # маршруты core
│   └── admin.py            # регистрация в админ-панели
├── reference_manager/
│   ├── settings.py
│   └── urls.py             # root-URLconf
├── manage.py
├── requirements.txt
└── README.md
```

---

## HTML-интерфейс

### Главная страница (`/`)

- Три Bootstrap-карточки-формы для добавления:
  1. Фабрика
  2. Участок (с выпадающим списком фабрик)
  3. Оборудование (с множественным выбором участков)
- Три таблицы:
  - **Фабрики**: ID, Name
  - **Участки**: №, Name, Factory
  - **Оборудование**: №, Name, badges(Участки), badges(Фабрики)
- **JS-логика**:
  - AJAX-запросы на `/api/.../`
  - Динамический `insertAdjacentHTML` для новых строк и `<option>` в селектах
  - Сортировка записей по фабрикам/участкам + автоматическая перенумерация колонок `№`

### Страница иерархии (`/hierarchy/<model>/<id>/`)

Показывает списки всех родителей и детей выбранного объекта (произвольная глубина).

---

## Админ-панель

Django Admin доступен по `/admin/` для быстрого управления справочниками.

---

