import os
import json
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.accounts.models import Employer, JobSeeker
from apps.jobs.models import Job, Category

User = get_user_model()

def clear_existing_data():
    print("Clearing existing dummy data...")
    # Delete all jobs, employers, and job seekers to start fresh
    Job.objects.all().delete()
    Employer.objects.all().delete()
    JobSeeker.objects.all().delete()
    # Delete users that are not superusers
    User.objects.filter(is_superuser=False).delete()
    print("Existing data cleared.")

def load_data_from_json(json_file_path):
    print(f"Loading data from {json_file_path}...")
    
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 1. Create Categories
    print("Creating categories...")
    for cat_data in data.get('categories', []):
        Category.objects.get_or_create(
            name=cat_data['name'], 
            defaults={'icon': cat_data['icon']}
        )

    # 2. Create Employers
    print("Creating employers...")
    employer_dict = {}
    for emp_data in data.get('employers', []):
        user = User.objects.create_user(
            username=emp_data['username'],
            email=emp_data['email'],
            password=emp_data['password'],
            is_employer=True,
            is_active=True
        )
        emp = Employer.objects.create(
            user=user,
            company_name=emp_data['company_name'],
            company_description=emp_data['description'],
            location=emp_data['location'],
            industry=emp_data['industry']
        )
        employer_dict[emp_data['username']] = emp

    # 3. Create Job Seekers
    print("Creating job seekers...")
    for js_data in data.get('job_seekers', []):
        user = User.objects.create_user(
            username=js_data['username'],
            email=js_data['email'],
            password=js_data['password'],
            is_job_seeker=True,
            is_active=True
        )
        JobSeeker.objects.create(
            user=user,
            skills=js_data['skills'],
            experience=js_data['experience'],
            education=js_data['education']
        )

    # 4. Create Jobs
    print("Creating jobs...")
    for job_data in data.get('jobs', []):
        employer = employer_dict.get(job_data['employer_username'])
        category = Category.objects.filter(name=job_data['category_name']).first()
        
        if employer and category:
            Job.objects.create(
                title=job_data['title'],
                employer=employer,
                category=category,
                description=job_data['description'],
                requirements=job_data['requirements'],
                location=job_data['location'],
                salary=job_data['salary'],
                job_type=job_data['job_type'],
                experience_level=job_data['experience_level']
            )
        else:
            print(f"Skipping job {job_data['title']} - Employer or Category not found.")

    print("Data loading complete!")

if __name__ == "__main__":
    clear_existing_data()
    load_data_from_json('dummy_data.json')
