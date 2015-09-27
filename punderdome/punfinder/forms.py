from django import forms

class NameForm(forms.Form):
	pun_me = forms.CharField(label='Your name', max_length=100)

