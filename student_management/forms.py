from django import forms
from .models import User
from admin_dash.models import Questions

ANS_CHOICES= [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ]
class RegistrationForm(forms.ModelForm):
    regd_id=forms.CharField(widget=forms.TextInput(attrs={'class':'','id':'regd_id','placeholder':'Registration ID'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'email','id':'email','placeholder':'Email Address'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'name','id':'name','placeholder':'Full Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'id':'password', 'placeholder': 'Password'}))
    class Meta:
        model=User
        fields=[
            'course',
			'regd_id',
            'name',
            'email',
            'password',
        ]
class LoginForm(forms.Form):
	regd_id=forms.CharField(widget=forms.TextInput(attrs={'class':'','id':'regd_id','placeholder':'Registration ID'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'id':'password', 'placeholder': 'Password'}))
    

	def clean(self,*args,**kwargs):
		email=self.cleaned_data.get('email')
		regd_id=self.cleaned_data.get('regd_id')
		return super(LoginForm,self).clean(*args,**kwargs)

class ExamChoiceFrm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=[
            'paper',
        ]
class AnsChoice(forms.Form):
    ans= forms.CharField(label='Select an option', widget=forms.RadioSelect(choices=ANS_CHOICES))
    def clean(self,*args,**kwargs):
        ans=self.cleaned_data.get('ans')
        return super(AnsChoice,self).clean(*args,**kwargs)