from django.shortcuts import render
from .models import Lugat
# Create your views here.


def salom(request):
	soz = request.GET.get('q' ,'')

	if soz and soz!='':
		natija = Lugat.objects.filter(xorazmcha__contains=soz).all()[:3]
	else:
		natija = None

	context = {
		'q':soz,
		'natija':natija
	}
	return render(request ,'home.html' , context)
