from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");





def index(request):
	return render(request,"appCodeCollections/index.html");

def edittables(request):
	return render(request,"appCodeCollections/404.html");

def codesubmissions(request):
	return render(request,"appCodeCollections/404.html");

def problemsubmissions(request):
	return render(request,"appCodeCollections/404.html");



def addproblems(request):
	return render(request,"appCodeCollections/404.html");

def addsolutions(request):
	return render(request,"appCodeCollections/404.html");

def addproblemsandsolutions(request):
	return render(request,"appCodeCollections/404.html");

def editproblems(request):
	return render(request,"appCodeCollections/404.html");

def editsolutions(request):
	return render(request,"appCodeCollections/404.html");

def problemswholelist(request):
	return render(request,"appCodeCollections/404.html");

def openproblemsandsolutions(request):
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















