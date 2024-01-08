from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['toipc_name','email','name']
        #exclude=['url']
        #labels={'topic_name':'TN'}
        widgets={'email':forms.PasswordInput}

