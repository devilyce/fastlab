from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'name'}))
    from_email = forms.EmailField(required=True,
                                  widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'from_email'}))
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'subject'}))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'name': 'message', 'rows': '10'}))
