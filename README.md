# 🎓 Student Registration System

[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)](https://getbootstrap.com/)

A complete Django-based Student Registration System with image upload, search functionality, and beautiful responsive UI. Perfect for schools, colleges, and educational institutions.

## ✨ Features

- 📝 **Student Registration** - Complete form with auto-generated ID
- 🖼️ **Image Upload** - Profile pictures with automatic renaming
- 🔍 **Search** - Search by name, registration number, or email
- 📊 **CRUD Operations** - Create, Read, Update, Delete students
- 📱 **Responsive Design** - Works on all devices
- 🔐 **Admin Panel** - Built-in Django admin interface
- ✅ **Form Validation** - Email confirmation, age verification

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Django 4.x | Backend Framework |
| Python 3.8+ | Programming Language |
| SQLite | Database |
| Bootstrap 5 | Frontend UI |
| Font Awesome | Icons |
| Pillow | Image Processing |

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager


###  Registration Form: http://127.0.0.1:8000/

###  Student List: http://127.0.0.1:8000/students/

### student-registration-system/
├── registration/           # Main application
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── forms.py           # Form validation
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin interface
├── templates/              # HTML templates
│   ├── base.html
│   └── registration/
├── media/                  # Uploaded images
├── static/                 # Static files
├── requirements.txt        # Dependencies
└── manage.py              # Django management
