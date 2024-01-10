from django import forms
    
def validation_for_letter(data):
    if data.lower().startswith('b'):
        raise forms.ValidationError('started with b')

def validate_length(data):
    if len(data)<3:
        raise forms.ValidationError('len is < 3')        




class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validation_for_letter,validate_length])
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['renteremail']
        if e!=re:
            raise forms.ValidationError('emails not matched')    