from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentRegistrationForm

def register_student(request):
    """Handle student registration"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.full_name} registered successfully! Registration Number: {student.registration_number}')
            return redirect('registration_success', student_id=student.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def registration_success(request, student_id):
    """Show success page with student details"""
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'registration/success.html', {'student': student})

def student_list(request):
    """List all registered students"""
    students_list = Student.objects.filter(is_active=True)
    paginator = Paginator(students_list, 10)  # Show 10 students per page
    
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    
    return render(request, 'registration/student_list.html', {'students': students})

def student_detail(request, student_id):
    """Show detailed information of a student"""
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'registration/student_detail.html', {'student': student})

def edit_student(request, student_id):
    """Edit student information"""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student.full_name} updated successfully!')
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentRegistrationForm(instance=student)
    
    return render(request, 'registration/edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    """Delete a student record"""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student_name = student.full_name
        student.delete()
        messages.success(request, f'Student {student_name} has been deleted.')
        return redirect('student_list')
    
    return render(request, 'registration/delete_confirm.html', {'student': student})

def search_students(request):
    """Search students by name, registration number, or email"""
    query = request.GET.get('q', '')
    students = Student.objects.filter(
        models.Q(full_name__icontains=query) |
        models.Q(registration_number__icontains=query) |
        models.Q(email__icontains=query)
    )
    
    return render(request, 'registration/student_list.html', {'students': students, 'search_query': query})