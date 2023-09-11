from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from appCodeCollections.models import *
import appCodeCollections.collections.BulkViewFunctions as BulkViewFunctions
import appCodeCollections.collections.BuildFilePaths as BuildFilePaths
from django.contrib import messages

from appCodeCollections.serializers import ProblemsSerializer

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import json





def problem(request,id=None):
	if ( id==None ):
		return JsonResponse({
				'error' : 'You not provide id here!!!'
		})

	problems = Problems.objects.filter(id=id)   #or, pk


def problem(request,id=None):
	if ( id==None ):
		return JsonResponse({
				'error' : 'You not provide id here!!!'
		})

	permit = bool(Problems.objects.filter(id=id))   #or, pk
	print(permit)
	if(not permit):
		return JsonResponse({
				'message' : 'This id is not available in the problem database.'
		})

	problem = Problems.objects.get(id=id)
	serializer = ProblemsSerializer(problem)
	return JsonResponse(serializer.data,safe=False)
 

def problems(request):
	problems = Problems.objects.all()
	serializer = ProblemsSerializer(problems,many=True)
	return JsonResponse(serializer.data,safe=False)
 













