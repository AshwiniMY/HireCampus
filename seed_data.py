import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.accounts.models import Employer, JobSeeker
from apps.jobs.models import Job, Category
from django.utils import timezone

User = get_user_model()

def seed_data():
    print("Starting data seeding...")

    # 1. Create Categories
    categories = ['Software Development', 'Design', 'Marketing', 'Data Science', 'Human Resources']
    icons = ['fas fa-code', 'fas fa-paint-brush', 'fas fa-ad', 'fas fa-database', 'fas fa-users']
    category_objs = []
    
    for name, icon in zip(categories, icons):
        cat, created = Category.objects.get_or_create(name=name, defaults={'icon': icon})
        category_objs.append(cat)
        if created:
            print(f"Created category: {name}")

    # 2. Create Employers
    employers_data = [
        {
            'username': 'tcs_recruiter',
            'email': 'recruiter@tcs.com',
            'company_name': 'TCS',
            'description': 'A global leader in IT services, consulting, and business solutions.',
            'location': 'Mumbai, Maharashtra',
            'industry': 'IT Services'
        },
        {
            'username': 'infosys_hr',
            'email': 'hr@infosys.com',
            'company_name': 'Infosys',
            'description': 'A global leader in next-generation digital services and consulting.',
            'location': 'Bengaluru, Karnataka',
            'industry': 'IT Services'
        }
    ]

    employer_objs = []
    for data in employers_data:
        user, created = User.objects.get_or_create(
            username=data['username'],
            defaults={
                'email': data['email'],
                'is_employer': True,
                'is_job_seeker': False,
                'is_active': True
            }
        )
        user.set_password('pass1234')
        user.save()
            
        emp, emp_created = Employer.objects.get_or_create(
            user=user,
            defaults={
                'company_name': data['company_name'],
                'company_description': data['description'],
                'location': data['location'],
                'industry': data['industry']
            }
        )
        employer_objs.append(emp)
        if created:
            print(f"Created employer user: {data['username']}")

    # 3. Create Job Seekers
    seekers_data = [
        {
            'username': 'ashwin_dev',
            'email': 'ashwin@example.com',
            'skills': 'Python, Django, SQL',
            'experience': '2 years as Software Engineer',
            'education': 'B.E. in Computer Science'
        },
        {
            'username': 'priya_design',
            'email': 'priya@example.com',
            'skills': 'UI/UX Design, Figma',
            'experience': '3 years as Visual Designer',
            'education': 'Bachelor of Fine Arts'
        }
    ]

    for data in seekers_data:
        user, created = User.objects.get_or_create(
            username=data['username'],
            defaults={
                'email': data['email'],
                'is_job_seeker': True,
                'is_employer': False,
                'is_active': True
            }
        )
        user.set_password('pass1234')
        user.save()
            
        JobSeeker.objects.get_or_create(
            user=user,
            defaults={
                'skills': data['skills'],
                'experience': data['experience'],
                'education': data['education']
            }
        )
        if created:
            print(f"Created seeker user: {data['username']}")

    # 4. Create Jobs
    jobs_data = [
        {
            'title': 'Full Stack Developer',
            'employer': employer_objs[0],
            'category': category_objs[0],
            'description': 'Looking for a skilled developer to work on enterprise applications.',
            'requirements': 'Expertise in Django and React.',
            'location': 'Bengaluru, India',
            'salary': '₹8,00,000 - ₹12,00,000',
            'job_type': 'full_time',
            'experience_level': 'mid'
        },
        {
            'title': 'UI/UX Designer',
            'employer': employer_objs[1],
            'category': category_objs[1],
            'description': 'Join our creative team to design intuitive user experiences.',
            'requirements': 'Strong portfolio in Figma and Adobe Suite.',
            'location': 'Hyderabad, India',
            'salary': '₹6,00,000 - ₹10,00,000',
            'job_type': 'full_time',
            'experience_level': 'mid'
        }
    ]

    for data in jobs_data:
        job, created = Job.objects.get_or_create(
            title=data['title'],
            employer=data['employer'],
            defaults={
                'category': data['category'],
                'description': data['description'],
                'requirements': data['requirements'],
                'location': data['location'],
                'salary': data['salary'],
                'job_type': data['job_type'],
                'experience_level': data['experience_level']
            }
        )

        if created:
            print(f"Created job: {data['title']}")

    print("Data seeding complete!")

if __name__ == "__main__":
    seed_data()
