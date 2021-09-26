from django import forms


class UserDataForm(forms.Form):
	text_data=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
	file_data=forms.ImageField()
	password=forms.CharField()



class UserDecodeForm(forms.Form):
	file_data=forms.ImageField()
	password=forms.CharField()