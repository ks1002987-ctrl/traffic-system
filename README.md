# 🚦 Traffic Management System (Flask + SQLite)

A simple, beginner-friendly web app to record and view traffic data.

## Features
- Add traffic data: **location, vehicle count, signal status** (Red/Yellow/Green)
- Stores data in a local **SQLite** database (`traffic.db`)
- Displays records in a clean HTML **table**
- Delete records with one click
- Uses Jinja2 **HTML templates** with a shared base layout

## Project Structure
```
traffic_system/
├── app.py              # Flask app + routes + DB code
├── requirements.txt    # Python dependencies
├── traffic.db          # SQLite DB (auto-created on first run)
└── templates/
    ├── base.html       # Shared layout (header, styles)
    ├── index.html      # Table of records
    └── add.html        # Form to add a record
```

## Setup & Run

1. **Install Python 3.8+**
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser at: **http://127.0.0.1:5000**

The database file `traffic.db` is created automatically the first time you run the app.

## How it works
- `app.py` defines three routes:
  - `/` — list all traffic records
  - `/add` — form to add a new record (GET shows form, POST saves it)
  - `/delete/<id>` — delete a record by id
- `init_db()` creates the `traffic` table if it doesn't exist.
- Templates use `{% extends "base.html" %}` so styling stays consistent.

Have fun! 🚗💨
