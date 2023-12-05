from django.shortcuts import render, redirect
from django.contrib import messages
from .form import * 
from .models import * 
from django.contrib.auth import get_user_model

User = get_user_model()

def dashboard(request):
    reviews = Review.objects.filter(user=request.user)
    context = {'reviews':reviews}
    return render(request, 'dashboard/dashboard.html', context)


def leave_review(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        form = LeaveReviewForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = user 
            var.save()
            messages.success(request, f'Your review has been recorded and anonymously shared with {user}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('leave-review')
    else:
        form = LeaveReviewForm
        context = {'form':form}
    return render(request, 'dashboard/leave_review.html', context)