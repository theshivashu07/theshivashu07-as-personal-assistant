

from appCodeCollections.models import *
# import appCodeCollections.models as MODELs
import appCodeCollections.collections._default as DEFAULTs

# this library is helpful for moving files one-place to another-place
import shutil

import os




def assignProblem(object,ProblemsDataStructures,wholeStatement):
	# lets create files for problem-input.
	object.filename = buildProblemFilePath(object,ProblemsDataStructures)
	object.save()  #must to save this, so that it also save on the main place.
	with open( f"{DEFAULTs.problems_location}\\{object.filename}" , 'wb' ) as file: 
		# actually below we converting normal-text-data to a binary-data.
		file.write(wholeStatement.encode(encoding="ascii",errors="xmlcharrefreplace"))
		# file.write(wholeStatement.encode(encoding="ascii",errors="xmlcharrefreplace"))  #original-things
	return

def assignSolution(object,SolutionsProgrammingLanguage,wholeCode):
	# lets create files for solution-input.
	object.filename = buildSolutionFilePath(object,SolutionsProgrammingLanguage)
	object.save()  #must to save this, so that it also save on the main place.
	with open( f"{DEFAULTs.solutions_location}\\{object.filename}" , 'wb' ) as file:
		# actually below we converting normal-text-data to a binary-data.
		file.write(wholeCode.encode("ascii",errors="xmlcharrefreplace"))
	return

def getProblem(object):
	# lets get files data, to show-case
	with open( f"{DEFAULTs.problems_location}\\{object.filename}" , 'rb' ) as file:
		# actually below we converting normal-text-data to a binary-data, with line change.
		withoutLineChange = file.read().decode("ascii",errors="xmlcharrefreplace")
		withLineChange=  '<br>'.join( withoutLineChange.split('\n') )
		object.detailsset=[withLineChange,withoutLineChange]
	return

def getSolution(object):
	# lets create files for solution-input.
	with open( f"{DEFAULTs.solutions_location}\\{object.filename}" , 'rb' ) as file:
		# actually below we converting normal-text-data to a binary-data.
		object.codesubmissions = file.read().decode("ascii",errors="xmlcharrefreplace")
	return





def buildProblemFilePath(object,ProblemsDataStructures):
	# wents like ---> "0001 - remove-duplicates-from-an-unsorted-linked-list - #geeksforgeeks #leetcode.txt"
	filepath = str(object.id).zfill(4) + ' - '
	filepath += object.slug + ' -'
	for id in ProblemsDataStructures:
		string = DataStructures.objects.get(id=id).name
		filepath += " #" + string.replace(" ", "").lower()
	filepath += '.txt'
	return filepath

def buildSolutionFilePath(object,SolutionsProgrammingLanguage):
	# wents like ---> "0001-000001 - remove-duplicates-from-an-unsorted-linked-list - #python.py"
	filepath = str(object.problem_id.id).zfill(4) + '-'
	filepath += str(object.id).zfill(6) + ' - '
	filepath += object.problem_id.slug + ' - '
	# here is we know that one solution have only one programming language, so there is simple...
	plObject = ProgrammingLanguages.objects.get(id=SolutionsProgrammingLanguage)
	filepath += "#" + plObject.name.lower()
	filepath += plObject.extension
	return filepath




def editProblems(objectProblem):
	"""because we already coming to edit-problem, means we have new data, so better thing that I delete old existing file..."""
	os.remove(f"{DEFAULTs.problems_location}\\{objectProblem.filename}")
	return 

def editSolutions(objectSolution):
	"""because we already coming to edit-solution, means we have new data, so better thing that I delete old existing file..."""
	os.remove(f"{DEFAULTs.solutions_location}\\{objectSolution.filename}")
	return 



def deleteProblemsAndSolutions(objectProblem):
	shutil.move(f"{DEFAULTs.problems_location}\\{objectProblem.filename}", f"{DEFAULTs.deleted_problems_location}\\{objectProblem.filename}")
	for object in Solutions.objects.all():
		if(object.problem_id == objectProblem):
			deleteSolutions(object)
	return 

def deleteSolutions(objectSolution):
	shutil.move(f"{DEFAULTs.solutions_location}\\{objectSolution.filename}", f"{DEFAULTs.deleted_solutions_location}\\{objectSolution.filename}")
	return 







def addLinks(objectProblem,ProblemsLinks):
	for i in range(0,len(ProblemsLinks),3):
		plateform_id,link,text=ProblemsLinks[i:i+3]
		if(plateform_id!='' and link!=''): 
			object = problems_links()
			object.problem_id = objectProblem
			object.plateform_id = Plateforms.objects.get(id=plateform_id)
			object.link = link
			object.text = text
			object.save()
	return 

def getLinks(objectProblem):
	objects = problems_links.objects.filter(problem_id=objectProblem) 
	datalist = list() 
	for object in objects: 
		datalist.append( [object.problem_id, object.plateform_id, object.link, object.text] ) 
	return datalist 



def addAttachments(objectProblem,objectSolution,ProblemsLinks):
	for i in range(0,len(ProblemsLinks),3):
		showntitle,link,note=ProblemsLinks[i:i+3]
		if(showntitle!='' and link!=''): 
			object = SolutionsAttachments()
			object.problem_id = objectProblem
			object.showntitle = showntitle
			object.link = link
			object.note = note
			object.save()
			newobject = SolutionAndSolutionsAttachments()
			newobject.problem_id = objectProblem
			newobject.solution_id = objectSolution
			newobject.solutionattachments_id = object
			newobject.save()
	return 

def getAttachments(objectProblem,objectSolution):
	objects = SolutionAndSolutionsAttachments.objects.filter(solution_id=objectSolution) 
	datalist = list() 
	for object in objects: 
		object = object.solutionattachments_id
		datalist.append( [object.problem_id, object.showntitle, object.link, object.note] ) 
	return datalist 



def addAnotherAttachments(objectProblem,objectSolution,SolutionsAnotherAttachments):
	getted = SolutionsAttachments.objects.get(id=SolutionsAnotherAttachments)
	object = SolutionAndSolutionsAttachments()
	object.problem_id = objectProblem
	object.solution_id = objectSolution
	object.solutionattachments_id = getted
	object.save()
	print(object)
	print(getted, SolutionsAnotherAttachments)
	return 

def getAnotherAttachments(objectProblem,objectSolution):
	objects = SolutionsAttachments.objects.filter(problem_id=objectProblem) 
	SASA = SolutionAndSolutionsAttachments.objects.filter(problem_id=objectProblem) 
	listOf = set(  object.solutionattachments_id for object in SASA if object.solution_id == objectSolution  ) 



	# getted = SolutionsAttachments.objects.filter(problem_id=objectProblem) 
	# listOfAttachments = set()
	#objects = SolutionAndSolutionsAttachments.objects.filter(problem_id=objectProblem) 
	#listOf = set( [ object.solutionattachments_id for object in objects if object.solution_id == objectSolution ] )
	datalist = list() 
	for object in objects: 
		# print(object.solution_id, objectSolution, object.solution_id != objectSolution)
		# print(object.solution_id.id, objectSolution.id, object.solution_id != objectSolution)
		if object.id not in listOf:
			datalist.append( object ) 
	return datalist 




