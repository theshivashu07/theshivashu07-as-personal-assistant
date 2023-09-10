from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from appCodeCollections.models import *
import appCodeCollections.collections.BulkViewFunctions as BulkViewFunctions
import appCodeCollections.collections.BuildFilePaths as BuildFilePaths
from django.contrib import messages


from django.http import JsonResponse
import json





def problem(request,id=None):
	if ( id==None ):
		return JsonResponse({
				'error' : 'You not provide id here!!!'
		})

	get = Problems.objects.filter(id=id)   #or, pk
	if(not get):
		return JsonResponse({
				'message' : 'This id is not available in the problem database.'
		})

	print(Problems.objects.get(id=id))
	return JsonResponse({
			'dataset' : json.loads(Problems.objects.get(id=id))
	})
 

def problems(request):
	data =  [ {1:'shivam', 2 : 'shri'}, {'a':'Aparna', 'r':'Renu'} ]
	data = Problems.objects.values_list('title')
	data = Problems.objects.values()
	return JsonResponse({
			'dataset' : json.loads(data)
	})
 













