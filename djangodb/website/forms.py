#step 17

from django import forms
from .models import Member

#step 18

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'passwd', 'age']