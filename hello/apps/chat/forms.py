from django import forms

class FeedBackForm(forms.Form):
	name = forms.CharField(label="Имя пользователя", max_length=150)
	email = forms.EmailField(label="email")
	description = forms.CharField(label="Текст")

# Нужно сделать блок для отправки писем на почту