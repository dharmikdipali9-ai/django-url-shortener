# 🔗 Django URL Shortener

A simple and efficient URL shortener built with Django and PostgreSQL.
It allows users to convert long URLs into short, shareable links.

---

## 🚀 Live Demo

👉 https://django-url-shortener-wvp1.onrender.com/

---

## 🛠️ Tech Stack

* Backend: Python, Django
* Database: PostgreSQL
* Deployment: Render
* Cloud DB: Supabase (Transaction Pooler)

---

## ✨ Features

* 🔗 Shorten long URLs instantly
* ⚡ Fast redirection to original links
* 🗄️ PostgreSQL database integration
* 🌐 Deployed and accessible online
* 🔒 Production-ready configuration

---

## 📂 Project Structure

```
shortener/
│── shortener/        # Main project settings
│── urls/             # App handling URL logic
│── templates/        # HTML templates
│── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/dharmikdipali9-ai/django-url-shortener.git
cd url-shortener
```

---

### 2. Create virtual environment

```bash
python -m venv .env
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres.gtusizmggkuizezyalvp:.Xwx6%3F%40zJ%3Fa5FWX@aws-1-ap-southeast-2.pooler.supabase.com:6543/postgres
SECRET_KEY=url_shortener
DEBUG=True
```

---

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Run server

```bash
python manage.py runserver
```

---

## 🌍 Deployment (Render)

* Connected GitHub repo to Render
* Added environment variables:

  * `DATABASE_URL`
  * `SECRET_KEY`
  * `DEBUG=False`
* Used Gunicorn for production server
* Automated migrations via build command

---

## 🧠 Key Learnings

* Django + PostgreSQL integration
* Handling environment variables securely
* Deploying full-stack apps on Render
* Debugging real-world deployment issues

---

## 🔮 Future Improvements

* 📊 Click analytics (track number of visits)
* 🧾 User authentication
* ✏️ Custom short URLs
* ⏳ Link expiration

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📧 Contact

Dipali Dharmik
📩 [dharmikdipali9@gmail.com](mailto:dharmikdipali9@gmail.com)
🔗 LinkedIn: https://linkedin.com/in/dipalidharmik

---

⭐ If you like this project, give it a star!
