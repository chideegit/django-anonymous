from django.shortcuts import render, redirect
from django.contrib import messages
from .form import * 
from .models import * 
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def dashboard(request):
    reviews = Review.objects.filter(user=request.user).order_by('-timestamp')
    context = {'reviews':reviews}
    return render(request, 'dashboard/dashboard.html', context)


def leave_review(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = LeaveReviewForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = user 
            var.save()
            messages.success(request, f'Your review has been recorded and anonymously shared with {user}')
            return redirect('completed')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('leave-review')
    else:
        form = LeaveReviewForm
        context = {'form':form, 'user':user}
    return render(request, 'dashboard/leave_review.html', context)

def completed(request):
    return render(request, 'dashboard/completed.html')