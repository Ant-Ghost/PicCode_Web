from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserDataForm, UserDecodeForm
from .models import PicModel
from .encode import Encode_Image
from .decode import Decode_Image
from django.conf import settings



# Create your views here.
def home(request):
	#print(request)
	return render(request, 'steg/home.html')



def decode(request):
	#print(request)
	context={}
	context['title']='Decode'
	if (request.method=='POST'):
		form=UserDecodeForm(request.POST, request.FILES)
		if form.is_valid():
			di=Decode_Image()
			image=form.cleaned_data['file_data']
			psswd=form.cleaned_data['password']
			obj=PicModel.objects.create(img=image)
			obj.save()
			location=(settings.MEDIA_ROOT+"\\"+(obj.img.name).replace('/','\\'))
			di.stegano_decode(location,psswd)
			if di.error_decode[0]==-1:
				context['error']=di.error_decode[1]
			else:
				context['text']=di.decode_text
		else:
			context['error']="form not valid"
			form=UserDecodeForm()
	else:
		form=UserDecodeForm()
	context['forms']=form
	context['fixed']='1'
	print(context)
	return render(request, 'steg/decode.html',context)



def encode(request):
	#print(request)
	context={}
	context['title']='Encode'
	if (request.method == 'POST'):
		form=UserDataForm(request.POST, request.FILES)
		if form.is_valid():
			ei=Encode_Image()
			text = form.cleaned_data['text_data']
			image = form.cleaned_data['file_data']
			psswd=form.cleaned_data['password']
			obj=PicModel.objects.create(img=image)
			obj.save()
			location=((settings.MEDIA_ROOT+"\\"+(obj.img.name).replace('/','\\')))
			ei.stegano_encode(text,psswd,location)
			if ei.error_encode[0]==1:
				context['error']=ei.error_encode[1]
			else:
				context['image']=obj.img.url
			
		else:
			print("form is not valid")
			context['error']="form not valid"
			form=UserDataForm()
	else:
		form=UserDataForm()
	context['forms']=form
	print(context)
	return render(request, 'steg/encode.html',context)


