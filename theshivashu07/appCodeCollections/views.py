from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"appCodeCollections/index.html");

def edittables(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		comingData=request.POST["comingData"]
		if(comingFrom=='Plateform'):
			lock=Plateforms()
			lock.name=comingData;
			lock.save()
		elif(comingFrom=='DataStructure'):
			lock=DataStructures()
			lock.name=comingData;
			lock.save()
		elif(comingFrom=='ProgrammingLanguage'):
			lock=ProgrammingLanguages()
			lock.name=comingData;
			lock.save()
		else:
			print("Go to somewhere else.....")
		return redirect("/codecollections/edittables/")
	thisisReturningDatabase = {
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'DataStructures' : DataStructures.objects.all(), 
		'Plateforms' : Plateforms.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/edittables.html", thisisReturningDatabase);

def codesubmissions(request):
	return render(request,"appCodeCollections/404.html");

def problemsubmissions(request):
	return render(request,"appCodeCollections/404.html");



def addProblem(request): 
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def addSolution(request, problemslug):
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def addProblemAndSolution(request):
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def editProblem(request, problemslug):
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def editSolution(request, problemslug, solutionid):
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def problemsWholeList(request):
	thisisReturningDatabase = {
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/404.html", thisisReturningDatabase);

def ProblemWithSolution(request, problemslug, solutionid):
	thisisReturningDatabase = {
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/404.html", thisisReturningDatabase);



def openProblem(request):
	return render(request,"appCodeCollections/404.html");











 



'''

BULK - DATA - ASSIGNMENT

	if request.method=="POST":
		for key in _importantdatasets.Plateforms:
			locks=Plateforms()
			locks.name=key
			locks.save()
		count=0
		for key in _importantdatasets.DataStructures:
			count+=1
			if(count==15):
				break;
			locks=DataStructures()
			locks.name=key
			locks.save()
		for key in _importantdatasets.ProgrammingLanguages:
			locks=ProgrammingLanguages()
			locks.name=key
			locks.save()
		return redirect("/codecollections/edittables/")
'''















