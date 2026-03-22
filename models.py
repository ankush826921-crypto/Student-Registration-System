from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, RegexValidator
import os

def student_image_path(instance, filename):
    """Generate path for uploaded student images"""
    ext = filename.split('.')[-1]
    filename = f"{instance.registration_number}_{instance.full_name.replace(' ', '_')}.{ext}"
    return os.path.join('student_images', filename)

class Student(models.Model):
    # Personal Information
    registration_number = models.CharField(max_length=20, unique=True, verbose_name="Registration Number")
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ], verbose_name="Gender")
    
    # Contact Information
    email = models.EmailField(unique=True, validators=[EmailValidator()], verbose_name="Email Address")
    phone_number = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be valid")],
        verbose_name="Phone Number"
    )
    address = models.TextField(verbose_name="Address")
    
    # Academic Information
    course = models.CharField(max_length=50, choices=[
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('BUS', 'Business Administration'),
        ('MED', 'Medicine'),
        ('LAW', 'Law'),
        ('ART', 'Arts'),
    ], verbose_name="Course")
    semester = models.IntegerField(choices=[(i, f'Semester {i}') for i in range(1, 9)], verbose_name="Semester")
    
    # Additional Information
    student_image = models.ImageField(upload_to=student_image_path, blank=True, null=True, verbose_name="Student Photo")
    parent_name = models.CharField(max_length=100, verbose_name="Parent/Guardian Name")
    parent_contact = models.CharField(max_length=15, verbose_name="Parent Contact Number")
    
    # Registration Details
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")
    is_active = models.BooleanField(default=True, verbose_name="Active Status")
    
    class Meta:
        ordering = ['-registration_date']
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self):
        return f"{self.full_name} ({self.registration_number})"
    
    def save(self, *args, **kwargs):
        if not self.registration_number:
            # Generate registration number if not provided
            import datetime
            year = datetime.datetime.now().year
            last_student = Student.objects.filter(registration_number__startswith=f"STU{year}").order_by('-registration_number').first()
            if last_student:
                last_num = int(last_student.registration_number[7:])
                new_num = last_num + 1
            else:
                new_num = 1
            self.registration_number = f"STU{year}{new_num:04d}"
        super().save(*args, **kwargs)
