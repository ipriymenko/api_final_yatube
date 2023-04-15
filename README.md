### Описание

#### API для социальной сети Yatube

функции:
- Получение, добавление, изменение и удаление постов;
- Получение, добавление, изменение и удаление комментариев к посту;
- Получение сообществ;
- Подписка и отписка на авторов;
- Авторизация по JWT: create, refresh, verify.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ipriymenko/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python -m venv env
```

Linux/macOS:
```
source env/bin/activate
```

Win:
```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация API и примеры запросов

После запуска сервера, перейти по ссылке http://127.0.0.1:8000/redoc/

