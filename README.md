# HireCampus
A modern, responsive platform designed to connect students and job seekers with employers efficiently.

**Live Demo:** [https://hirecampus.onrender.com](https://hirecampus.onrender.com)

## Setup
```bash
git clone https://github.com/AshwiniMY/HireCampus.git
cd hirecampus

# Setup Environment
python -m venv venv
# Windows: venv\Scripts\activate 
# Mac/Linux: source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Setup Database & Load Dummy Data
python manage.py migrate
python load_json_data.py

# Run Server
python manage.py runserver
```

## What it does
- **Dual User Roles:** Dedicated portals and functionality for both Job Seekers and Employers.
- **Quick Access Demo:** Pre-configured accounts and dummy data for easy portfolio review.
- **Modern UI:** Responsive and attractive interface built with Tailwind CSS.
- **Deploy Ready:** Prepared for free hosting deployment on platforms like Render.com.

## Tech used
Django (Python), SQLite, JavaScript, Tailwind CSS

## Author
Ashwini M Y — [LinkedIn](https://www.linkedin.com/in/ashwiniyaraguppi09/) | [GitHub](https://github.com/AshwiniMY)
