# Kittygram (starter)

Minimal Django REST Framework API for cats — the base template from which [kittygram_backend](https://github.com/Shipovmax/kittygram_backend) was developed.

> For the full-featured version with auth, achievements, image upload, and Docker deployment see [kittygram_final](https://github.com/Shipovmax/kittygram_final).

---

## What's here

- `Cat` model — `name`, `color`, `birth_year`
- `CatViewSet` — full CRUD via `ModelViewSet`
- `SimpleRouter` — routes registered at `/cats/`
- No auth, no pagination, no image upload

---

## Tech Stack

| | |
|---|---|
| Framework | Django 5.1, DRF 3.15 |
| Database | SQLite3 |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/kittygram
cd kittygram

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

API at `http://127.0.0.1:8000/cats/`

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
