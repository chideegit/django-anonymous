from django import forms 
from .models import * 

class LeaveReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['leave_review']