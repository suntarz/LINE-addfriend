# reckitt_app/forms.py

from django import forms
from .models import LineUser

class LineUserForm(forms.ModelForm):
    """แบบฟอร์มสำหรับการสร้างและแก้ไขข้อมูลผู้ใช้ LINE"""
    
    class Meta:
        model = LineUser
        fields = [
            'line_id', 'display_name', 'first_name', 'last_name', 
            'employee_id', 'department', 'picture_url'
        ]
        widgets = {
            'line_id': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'picture_url': forms.URLInput(attrs={'class': 'form-control'}),
        }