from django.shortcuts import render
from .import forms
# Create your views here.
def studentregisterview(request):
    form=forms.StudenRegistration()
    return render(request,'testApp/register.html',{'form':form})