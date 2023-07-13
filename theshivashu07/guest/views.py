from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.




def index(request):
	return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'> And your profile-username is '@theshivashu07'</b> !!!");














