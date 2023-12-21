from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
import appCodeCollections.collections.BulkViewFunctions as BulkViewFunctions
import appCodeCollections.collections.BuildFilePaths as BuildFilePaths
from django.contrib import messages





# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!"); 

def index(request):                                              
	return render(request,"appCodeCollections/index.html");   





def edittables(request): 
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		tracks = { 'Plateform':Plateforms(), 'DataStructure':DataStructures(), 'ProgrammingLanguage':ProgrammingLanguages(), 'DSASheetList':DSAsSheetsLists() }
		if(comingFrom in tracks):
			lock= tracks[comingFrom]
			if(comingFrom == 'DSASheetList'):
				lock.name = request.POST["comingName"]
				lock.by = request.POST["comingBy"]
				lock.reference = request.POST["comingReference"]
			else:
				lock.name=request.POST["comingData"]
			lock.save()
			messages.success(request, lock.name+" added on '"+comingFrom + "' Database.")
		return redirect("/codecollections/edit-tables/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	return render(request,"appCodeCollections/edittables.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def addProblem(request): 
	# problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":
		# termination-conditions  -  if problem already exist, then we move this to the oroginal problem side...
		objectProblemLists = Problems.objects.filter(title=request.POST["ProblemsTitle"])
		if(bool(objectProblemLists)):
			# we know that their is already one-problem exist with same name, so redirect on this...
			objectProblem = objectProblemLists[0] 
			messages.error(request, "Actually, same name's problem already exist in the database!!! See this opened problem...")
			return redirect("/codecollections/problem/"+objectProblem.slug+"/")

		# now this place is the safest place, so now add problem...
		object = BulkViewFunctions.AddProblems(request)
		messages.success(request, "New problem '" + object.title +"' is added.")

		# now we redirect our urls, according to pressed submit buttons...
		getting = request.POST["submit"]
		tracks = {  "Submit":"problem/"+object.slug+"/", "Submit + Add Solution":"add-solution/"+object.slug+"/", "Submit + Add More":"add-problem/"  }
		if(tracks.get(getting,0)):
			return redirect("/codecollections/"+tracks[getting])  
		# I know only three buttons in the options, but for play safe, I code below, otherwise its never coming situation!!!
		messages.error(request, "Must to visit you on code section, because you do some un-wanted thing.")
		return redirect("/")	

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def addSolution(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] == "" ):
			messages.error(request, "Solution's 'code' is must to add!!!")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
			thisisReturningDatabase.update( BulkViewFunctions.getbackSolutionDetails(request) )
			return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add solution...
		objectSolution = BulkViewFunctions.AddSolutions(request,objectProblem)
		messages.success(request, "Problem '" + objectProblem.title +"' solution is added.")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





'''
def addProblemAndSolution(request):
	if request.method=="POST":		
		# termination-conditions  -  if problem already exist, then we move this to the oroginal problem side...
		objectProblemLists = Problems.objects.filter(title=request.POST["ProblemsTitle"])
		if(bool(objectProblemLists)):
			# we know that their is only one problem exist with same name, thats-it...
			objectProblem = objectProblemLists[0] 
			messages.error(request, "Actually, same name's problem already exist in the database!!! See this opened problem...")
			return redirect("/codecollections/problem/"+objectProblem.slug+"/")

		# what if you put blank your problem's "title" or "detailsset", then we sent back to the same place again...
		# we'll I'm already managing this, with set 'required' in these field, but always play safe, may I'll be forgrt... 
		if( request.POST["ProblemsTitle"] == "" or request.POST["ProblemsDetailSet"] == "" ):
			messages.error(request, "Problems 'Title' and 'Statement' is must to add!!!  Please Re-Submit again!!!")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			thisisReturningDatabase.update( BulkViewFunctions.getbackProblemDetails(request) )
			thisisReturningDatabase.update( BulkViewFunctions.getbackSolutionDetails(request) )
			return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add problem...
		objectProblem = BulkViewFunctions.AddProblems(request)
		messages.success(request, "New problem '" + objectProblem.title +"' is added.")

		######################################################################################
		# SOLUTION's --------------------------------------------------------------------------------------------------------------------------------------------------
		if( request.POST["SolutionsCodeSubmissions"] == "" ):
			messages.error(request, "Solution's 'code' is must to add!!! Please fill all fields again...")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			return redirect("/codecollections/add-solution/"+objectProblem.slug+"/")
			# return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add solution...
		objectSolution = BulkViewFunctions.AddSolutions(request,objectProblem)
		messages.success(request, "Problem '" + objectProblem.title +"' solution is added.")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");
'''





def editProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] ):
			BuildFilePaths.editProblems(objectProblem)
			BulkViewFunctions.EditProblems(request,objectProblem)	
		else:
			print("This is not correct Input's... Reput again!!!")
		slug = Problems.objects.get(id=objectProblem.id).slug
		return redirect("/codecollections/problem/"+slug+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");


def editSolution(request, problemslug, solutionid):
	objectProblem=Problems.objects.get(slug=problemslug)
	objectSolution=Solutions.objects.get(id=solutionid)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			BuildFilePaths.editSolutions(objectSolution)
			BulkViewFunctions.EditSolutions(request,objectProblem,objectSolution.id)
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	thisisReturningDatabase['SolutionDataSet'] = BulkViewFunctions.SolutionDataSet(objectProblem,objectSolution.id)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def deleteProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	# move files to another folders for problem as-well-as its solutions
	BuildFilePaths.deleteProblemsAndSolutions(objectProblem)

	# after all tasks performing, delete this
	objectProblem.delete()
	return redirect("/codecollections/problems-with-solutions/")


def deleteSolution(request, problemslug, solutionid):
	objectSolution=Solutions.objects.get(id=solutionid)
	# move files to another folders for solutions
	BuildFilePaths.deleteSolutions(objectSolution)

	# update-SolutionsCount
	objectSolution.problem_id.SolutionsCount -= 1
	objectSolution.problem_id.save()

	# after all tasks performing, delete this
	objectSolution.delete()
	return redirect("/codecollections/problems-with-solutions/")










def addProblemsLinks(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		ProblemsLinks=request.POST.getlist("ProblemsLinks")
		BuildFilePaths.addLinks(objectProblem,ProblemsLinks)
		return redirect(f"/codecollections/problem/{objectProblem.slug}/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	thisisReturningDatabase['ProblemLinks'] = BuildFilePaths.getLinks(objectProblem)
	# return redirect("/codecollections/problem-links/", thisisReturningDatabase)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-links.html", thisisReturningDatabase);


def addSolutionsAttachments(request, problemslug, solutionid):
	objectProblem=Problems.objects.get(slug=problemslug)
	objectSolution=Solutions.objects.get(id=solutionid)
	if request.method=="POST":
		SolutionsAttachments=request.POST.getlist("SolutionsAttachments")
		BuildFilePaths.addAttachments(objectProblem,objectSolution,SolutionsAttachments)

		SolutionsAnotherAttachments=request.POST["SolutionsAnotherAttachments"]
		if SolutionsAnotherAttachments!="":
			BuildFilePaths.addAnotherAttachments(objectProblem,objectSolution,SolutionsAnotherAttachments)		
		return redirect(f"/codecollections/problem-solution/{objectProblem.slug}/{objectSolution.id}")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	thisisReturningDatabase['SolutionDataSet'] = BulkViewFunctions.SolutionDataSet(objectProblem,objectSolution.id)
	thisisReturningDatabase['SolutionAttachments'] = BuildFilePaths.getAttachments(objectProblem,objectSolution)
	thisisReturningDatabase['SolutionAnotherAttachments'] = BuildFilePaths.getAnotherAttachments(objectProblem,objectSolution)
	# return redirect("/codecollections/solution-attachments/", thisisReturningDatabase)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-attachments.html", thisisReturningDatabase);












def ProblemWithSolution(request, problemslug, solutionid):
	objectProblem=Problems.objects.get(slug=problemslug)

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	thisisReturningDatabase['SolutionDataSet'] = BulkViewFunctions.SolutionDataSet(objectProblem,solutionid)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-show.html", thisisReturningDatabase);



def openProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-show.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");






def fatchProblemsWithOrWithoutSolutions(request):
	if request.method=="POST":
		return redirect("/codecollections/"+ request.POST["problemselection"] +"/")
	tracks = {  
		'/codecollections/problems-with-or-without-solutions/':'__all__', 
		'/codecollections/problems-with-solutions/':'__with__', 
		'/codecollections/problems-without-solutions/':'__without__'  
	}
	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['AllProblemsSolutions'] = BulkViewFunctions.AllProblemWithOrWithoutSolutions(tracks[request.path])
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/wholelist.html", thisisReturningDatabase);





def openTestingPage(request):
	# return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/testingpage.html", thisisReturningDatabase);
	return render(request,"appCodeCollections/404.html");



 


def allProblemsLists(request):

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	holds = list()
	for object in Problems.objects.all():
		## below two lines are we apply when we have doubt that maybe we delete solutions by Admin, because on that situation SolutionsCount not have actual solution's count
		# object.SolutionsCount = len(Solutions.objects.filter(problem_id=object))
		# object.save() 
		object.links = dict() 
		object.links['problemslink'] = problems_links.objects.filter(problem_id=object)
		object.links['solutionslink'] = SolutionsAttachments.objects.filter(problem_id=object)
		holds.append(object)
	thisisReturningDatabase['ProblemDataSet'] = holds
	# thisisReturningDatabase['SolutionDataSet'] = BulkViewFunctions.SolutionDataSet(objectProblem,solutionid)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/wholeproblems.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");











 













