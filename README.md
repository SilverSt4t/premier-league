# Premier League Predictor

Aplikasi prediksi pertandingan Liga Inggris menggunakan **Machine Learning (RandomForest)** dan tampilan web **Django**.

## Struktur

- `prediction/` — modul prediksi skor & klasemen (Python + Tkinter GUI)
- `premier_project/` — aplikasi web Django (`manage.py`, `db.sqlite3`)

## Fitur
- Prediksi skor kandang & tandang
- Perhitungan klasemen otomatis
- Antarmuka grafis (Tkinter) + web (Django)

## Quick Start

```bash
# 1. Prediction module
pip install -r prediction/requirements.txt
python prediction/src/py/main.py

# 2. Django web
cd premier_project
pip install django pandas scikit-learn
python manage.py runserver
```

## Catatan
- Data prediksi disimpan di `prediction/data/`
- Database SQLite sudah ada di `premier_project/db.sqlite3`
