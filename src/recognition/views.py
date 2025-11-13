from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Recognition

# Student List View
@login_required
def student_list_view(request):
    students = User.objects.all()  # Get all users (students)
    return render(request, 'recognition/student_list.html', {'students': students})

# Recognition View (Sending credits to another student)
@login_required
def recognition_view(request, student_id):
    student = User.objects.get(id=student_id)
    if request.method == 'POST':
        credits = int(request.POST.get('credits'))
        if credits <= 0:
            messages.error(request, "Credits must be a positive number.")
        elif credits > 100:
            messages.error(request, "You cannot send more than 100 credits.")
        else:
            # Create recognition entry
            recognition = Recognition.objects.create(sender=request.user, receiver=student, credits=credits)
            recognition.save()
            messages.success(request, f"Successfully recognized {student.username} with {credits} credits!")
            return redirect('student_list')
    return render(request, 'recognition/recognition_form.html', {'student': student})
