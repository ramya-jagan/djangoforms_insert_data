from django import forms
from django.core import validators
    
def validation_for_letter(data):
    if data.lower().startswith('b'):
        raise forms.ValidationError('started with b')

def validate_length(data):
    if len(data)<3:
        raise forms.ValidationError('len is < 3')        




class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validation_for_letter,validators.MinLengthValidator(4)])
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['renteremail']
        if e!=re:
            raise forms.ValidationError('emails not matched')    

# used for avoiding automated server providing source code 
    # def clean_botcatcher(self):
       # b=self.cleaned_data['botcat'] 
       # if len(b)>0:
          #  raise forms.ValidationError('bot') 
