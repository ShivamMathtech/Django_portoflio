# Django Portfolio Website

A personal portfolio website built with Django and deployed on **Vercel**.

## 🚀 Features

- Simple and responsive portfolio layout
- Django backend with static files management
- Hosted on **Vercel** for easy deployment

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ShivamMathtech/portfolio.git
cd portfolio
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to check if it's running.

---

## 🚀 Deploy to Vercel

### 1️⃣ Install Vercel CLI

```bash
npm install -g vercel
vercel login
```

### 2️⃣ Create a `vercel.json` File

Create a **`vercel.json`** file in the root directory:

```json
{
  "builds": [{ "src": "portfolio/wsgi.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "portfolio/wsgi.py" }]
}
```

### 3️⃣ Update `ALLOWED_HOSTS`

In `portfolio/settings.py`, add your Vercel domain:

```python
ALLOWED_HOSTS = ['your-vercel-project.vercel.app', '127.0.0.1', 'localhost']
```

### 4️⃣ Deploy the Project

```bash
vercel --prod
```

Vercel will generate a live URL for your project. 🎉

---

## 🛠️ Common Issues & Fixes

### ❌ `DisallowedHost`

If you see this error:

```bash
Invalid HTTP_HOST header: 'your-vercel-project.vercel.app'.
```

Fix:

- Update `ALLOWED_HOSTS` in `settings.py` to include your Vercel domain.

### ❌ Static Files Not Loading

Fix:

```python
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

Run:

```bash
python manage.py collectstatic
```

---

## 📜 License

This project is open-source and free to use.

Happy Coding! 🚀
