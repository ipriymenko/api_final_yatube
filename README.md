## Описание

### API для социальной сети Yatube

функции:
- Получение, добавление, изменение и удаление постов;
- Получение, добавление, изменение и удаление комментариев к посту;
- Получение сообществ;
- Подписка на авторов;
- Авторизация по JWT: create, refresh, verify.


### Примеры запросов и ответов:

---
#### Получить список всех публикаций. 
```http
GET /api/v1/posts/
```
Ответ: `200`
```json
[
    {
        "id": 1,
        "author": "username",
        "text": "Добро пожаловать, ознакомьтесь с правилами отправки постов: ... ",
        "pub_date": "2021-10-14T20:41:29.648Z",
        "image": "http://api.example.org/media/posts/d628586d-174c-4e61-bb8a-7ca2e2a9dc90.png",
        "group": 1
    }
]
```
При указании параметров limit и offset выдача работает с пагинацией.
```http
GET /api/v1/posts/?offset=300&limit=100
```
Ответ: `200`
```json
{
    "count": 623,
    "next": "http://api.example.org/api/v1/posts/?offset=400&limit=100",
    "previous": "http://api.example.org/api/v1/posts/?offset=200&limit=100",
    "results": [
        {
            "id": 300,
            "author": "username",
            "text": "some text",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": null,
            "group": null
        }
    ]
}
```
---
### Создание поста

```http
POST /api/v1/posts/
```
```
Authorization: Bearer {{access token}}
```
payload - json. **Обязательное поле** `text`:
```json
{
    "text": "Текст поста!",
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICA==",
    "group": 1
}
```

Ответ: `201`
```json
{
    "id": 2,
    "author": "username",
    "text": "Текст поста!",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "http://127.0.0.1:8000/media/posts/d628586d-174c-4e61-bb8a-7ca2sdsd239dc90.png",
    "group": 1
}
```

---
Полная документация и больше примеров запросов по ссылке http://127.0.0.1:8000/redoc/
после запуска проекта.
---
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/ipriymenko/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv env
```

Linux/macOS:
```bash
source env/bin/activate
```

Win:
```bash
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver
```


