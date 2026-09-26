import email

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

PROJECTS = {

    'student-portal': {
        'title': 'School  Attendance Portal',

        'description':
            'A web-based student management system designed to manage student and teacher information and attendance records.',

        'documentation':
            'The School Attendance Portal is a web-based system built for managing and monitoring student and teacher attendance in a college setting. It provides administrators with tools to manage academic records (departments, courses, classes), maintain user accounts, and track daily attendance for both students and teaching staff.',

        'functionality':
            'The system allows users to manage student information, access academic data, and interact with information stored in the database.',
            

        'technologies': [
            'Next.js',
            'TypeScript',
            'React',
            'Prisma',
            'MySQL',
        ],
        'features': [
            'Role-based authentication for Admin, Teacher, and Student accounts with secure password hashing',
            'Department, course, and class management (e.g., CCS → BSIT/BSCS, CBA → BSBA)',
            'Student and teacher account creation with linked login credentials',
            'Daily attendance tracking with Present, Absent, Late, and Excused statuses',
            'Duplicate-safe attendance records to prevent multiple entries for the same attendance',
            'Filterable attendance reports by department and course',
            'Admin dashboard with real-time attendance and enrollment statistics',
],
        
        'screenshots': [
            'images/projects/project1/studentportal_ss1.png',
            'images/projects/project1/studentportal_ss2.png',
            'images/projects/project1/studentportal_ss3.png',
            'images/projects/project1/studentportal_ss4.png',
            'images/projects/project1/studentportal_ss5.png',
            'images/projects/project1/studentportal_ss6.png',
        ],
    },


    'django-portfolio': {
        'title': 'Django Portfolio',

        'description':
            'A personal portfolio website built using Django, HTML, CSS, and JavaScript.',

        'documentation':
            'The Django Portfolio is a personal website developed to present my software development projects, technical skills, and background in a clean and responsive interface. The website also provides detailed project pages where visitors can explore project descriptions, features, technologies, and screenshots.',

        'functionality':
            'The website provides a single-page portfolio experience with sections for my introduction, skills, projects, and contact information. Visitors can browse my projects, open dedicated project detail pages, view project screenshots in an enlarged image viewer, and send a message through the contact form.',

        'technologies': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'Git',
            'GitHub',
        ],
        'features': [
            'Responsive personal portfolio interface designed for desktop',
            'Single-page navigation with smooth scrolling between portfolio sections',
            'Project showcase displaying project descriptions, technologies, and screenshots'
            'Dedicated project detail pages with documentation, functionality, features, and technologies used',
            'Interactive project screenshot viewer for viewing images in an enlarged modal',
            'Skills section showcasing my programming languages, frameworks, and development tools',
            'Contact form that allows visitors to send messages directly through email',
            
        ],

        'screenshots': [
            'images/projects/project2/portfolio_ss1.png',
            'images/projects/project2/portfolio_ss2.png',
            'images/projects/project2/portfolio_ss3.png',
            'images/projects/project2/portfolio_ss4.png',
            'images/projects/project2/portfolio_ss5.png',
        ],
    },


    'e-commerce-website': {
        'title': 'E-Commerce Website',

        'description':
            'A web-based e-commerce system that allows customers to browse products, manage their shopping cart, place orders, and track their orders through assigned riders.',

        'documentation':
            'This E-Commerce Website was developed as a school project to provide an online shopping system where customers can browse available products such as beverages, add items to their shopping cart, place orders, and monitor the status of their purchases.',

        'functionality':
            'The system provides product management, product browsing, shopping cart functionality, order placement, and order management. Customers can also track the status of their orders through the rider assigned to their account, allowing them to monitor the progress of their delivery.',

        'technologies': [
            'Python',
            'Django',
            'SQLite',
            'HTML',
            'CSS',
            'JavaScript',
        ],
        'features': [
            'Product management for adding, editing, and deleting products',
            'Product browsing with search and filter options',
            'Shopping cart functionality for adding and removing products',
            'Order management for placing and tracking orders',
            'Customer order tracking',
            ],
        
        
        'screenshots': [
            'images/projects/project3/ecom_ss1.png',
            'images/projects/project3/ecom_ss2.png',
            'images/projects/project3/ecom_ss3.png',
            'images/projects/project3/ecom_ss4.png',
            'images/projects/project3/ecom_ss5.png',
        ],
    },

}

def project_detail(request, project_slug):

    project = PROJECTS.get(project_slug)

    if project is None:
        return render(
            request,
            '404.html',
            status=404
        )

    return render(
        request,
        'project_detail.html',
        {
            'project': project
        }
    )

def home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        visitor_email = request.POST.get('email')
        message = request.POST.get('message')

        email_message = f"""
You received a new message from your portfolio website.

Name: {name}
Email: {visitor_email}

Message:
{message}
"""

        email = EmailMessage(
            subject=f"Portfolio Contact: {name}",
            body=email_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[visitor_email],
        )

        email.send(fail_silently=False)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/#contact')


    return render(request, 'home.html')