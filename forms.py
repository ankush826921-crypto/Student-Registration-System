from django import forms
from .models import Student
from django.core.exceptions import ValidationError
import datetime

class StudentRegistrationForm(forms.ModelForm):
    confirm_email = forms.EmailField(label="Confirm Email", required=True)
    
    class Meta:
        model = Student
        fields = [
            'full_name', 'date_of_birth', 'gender', 'email', 'confirm_email',
            'phone_number', 'address', 'course', 'semester', 'student_image',
            'parent_name', 'parent_contact'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'confirm_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Confirm email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Parent's full name"}),
            'parent_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Parent's contact number"}),
            'student_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        
        if email and confirm_email and email != confirm_email:
            self.add_error('confirm_email', "Emails do not match.")
        
        date_of_birth = cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = datetime.date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 16:
                self.add_error('date_of_birth', "Student must be at least 16 years old.")
            if age > 100:
                self.add_error('date_of_birth', "Please enter a valid date of birth.")
        
        return cleaned_data