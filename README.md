# HireCampus 
A modern, responsive platform built with **Django** and **Tailwind CSS**. Designed to connect students and job seekers with employers efficiently.

### Tech Stack
**Django (Python)**  • **SQLite** • **Javascript** • **Tailwind CSS**

---
### Quick Demo
If you are reviewing this project for a portfolio, skip the sign-up! Use these pre-configured accounts:
*   **Password for all accounts:** `pass1234`
*   **Employer Login**: `wipro_hr` or `zomato_careers`
*   **Job Seeker Login**: `rahul_sharma` or `sneha_patel`

---
### How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AshwiniMY/HireCampus.git
   cd hirecampus
   ```
2. **Setup Environment & Install:**
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate 
   pip install -r requirements.txt
   ```
3. **Setup Database & Load Dummy Data:**
   ```bash
   python manage.py migrate
   python load_json_data.py
   ```
4. **Run Server:**
   ```bash
   python manage.py runserver
   ```
   *Go to `http://127.0.0.1:8000/` in your browser.*

---

### 🌐 How to Host for Free (Render.com)
1. Push this repository to your GitHub account.
2. Sign in to [Render.com](https://render.com) and create a new **Web Service**.
3. Connect your GitHub and select this repository.
4. **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python load_json_data.py`
5. **Start Command**: `gunicorn core.wsgi:application`
6. Click **Deploy**!
