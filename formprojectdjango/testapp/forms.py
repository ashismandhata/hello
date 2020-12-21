from django import forms
class StudenRegistration(forms.Form):
    name=forms.CharField(max_length=45)
    marks=forms.IntegerField()