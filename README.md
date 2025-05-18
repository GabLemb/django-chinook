# Django Chinook API

This project is a Django REST API for the [Chinook](https://github.com/lerocha/chinook-database) sample database. It provides endpoints for managing albums, artists, tracks, and playlists.

## Features

- Django 5.2 with Django REST Framework
- SQLite database (Chinook sample)
- CORS enabled for all origins
- CRUD endpoints for Albums, Artists, Tracks, and Playlists

## Project Structure

```
first/
    manage.py
    chinook.db
    schema.sql
    first/
        settings.py
        urls.py
        ...
    service/
        models.py
        serializers.py
        views.py
        urls.py
        ...
requirements.txt
```

## Setup

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd <repo-directory>
   ```

2. **Create and activate a virtual environment**

   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Database**

   - The project uses `chinook.db` (already included).
   - If you need to recreate it, use the provided `schema.sql`.

5. **Run migrations (if needed)**

   ```sh
   python first/manage.py migrate
   ```

6. **Run the development server**

   ```sh
   python first/manage.py runserver
   ```

## API Endpoints

All endpoints are prefixed with `/api/`.

| Resource  | Endpoint          |
| --------- | ----------------- |
| Albums    | `/api/albums/`    |
| Artists   | `/api/artists/`   |
| Tracks    | `/api/tracks/`    |
| Playlists | `/api/playlists/` |

Standard REST actions (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) are supported.

## CORS

CORS is enabled for all origins via [`CORS_ALLOW_ALL_ORIGINS = True`](first/first/settings.py).

## Development

- Main settings: [`first/first/settings.py`](first/first/settings.py)
- Models: [`first/service/models.py`](first/service/models.py)
- Serializers: [`first/service/serializers.py`](first/service/serializers.py)
- Views: [`first/service/views.py`](first/service/views.py)
- API URLs: [`first/service/urls.py`](first/service/urls.py)

## License

MIT

---

**Note:** This project is for educational/demo purposes and is not production-ready.
