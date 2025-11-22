from django import forms

class ExampleForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)