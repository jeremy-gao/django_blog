from django import forms
from blog.models import Contact
##

class ContactForm(forms.Form):
	name = forms.CharField(required=True,widget=forms.TextInput(attrs={'required':'required','placeholder':"Name"}));
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'required':'required','placeholder':"Email",'pattern':"[^@]*@[^@]*"}));
	phone = forms.CharField(widget=forms.TextInput(attrs={'required':'required','placeholder':"Phone"}));
	city = forms.CharField(widget=forms.TextInput(attrs={'required':'required','placeholder':"City Name"}));
	message = forms.CharField(required=True,widget=forms.Textarea(attrs={'required':'required','placeholder':"City Name",'type':"textarea"}));

	def save(self):
		name = self.cleaned_data['name'];
		email = self.cleaned_data['email'];
		phone = self.cleaned_data['phone'];
		city = self.cleaned_data['city'];
		message = self.cleaned_data['message'];
		return Contact.objects.create(name=name,email=email,phone=phone,city=city,message=message);