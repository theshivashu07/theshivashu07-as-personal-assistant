

from appCodeCollections.models import *
import appCodeCollections._DefaultValueSets as _DefaultValueSets






def assignProblem(object,ProblemsDataStructures,wholeStatement):
	# lets create files for problem-input.
	print("come-2")
	object.filename = buildProblemFilePath(object,ProblemsDataStructures)
	object.save()
	with open( f"{_DefaultValueSets.problems_location}\\{object.filename}" , 'wb' ) as file: 
		# actually below we converting normal-text-data to a binary-data.
		file.write(wholeStatement.encode('ascii'))
	print("come-5")
	return

def assignSolution(object,SolutionsProgrammingLanguage,wholeCode):
	# lets create files for solution-input.
	print("come-2")
	object.filename = buildSolutionFilePath(object,SolutionsProgrammingLanguage)
	object.save()
	with open( f"{_DefaultValueSets.solutions_location}\\{object.filename}" , 'wb' ) as file:
		# actually below we converting normal-text-data to a binary-data.
		file.write(wholeCode.encode('ascii'))
	print("come-5")
	return

def getProblem(object):
	# lets get files data, to show-case
	with open( f"{_DefaultValueSets.problems_location}\\{object.filename}" , 'rb' ) as file:
		# actually below we converting normal-text-data to a binary-data, with line change.
		object.detailsset=file.read().decode("ascii")
		object.detailsset =  '<br>'.join( object.detailsset.split('\n') )
	return

def getSolution(object):
	# lets create files for solution-input.
	with open( f"{_DefaultValueSets.solutions_location}\\{object.filename}" , 'rb' ) as file:
		# actually below we converting normal-text-data to a binary-data.
		object.codesubmissions = file.read().decode('ascii')
	return



def buildProblemFilePath(object,ProblemsDataStructures):
	# wents like ---> "0001 - remove-duplicates-from-an-unsorted-linked-list - #geeksforgeeks #leetcode.txt"
	print("come-3")
	filepath = ""
	filepath += str(object.id).zfill(4) + ' - '
	filepath += object.slug + ' -'
	for id in ProblemsDataStructures:
		string = DataStructures.objects.get(id=id).name
		filepath += " #" + string.replace(" ", "").lower()
	filepath += '.txt'
	print(f"<{object.filename}>")
	print("come-4")
	return filepath

def buildSolutionFilePath(object,SolutionsProgrammingLanguage):
	# wents like ---> "0001-01 - remove-duplicates-from-an-unsorted-linked-list - #python.py"
	# wents like ---> "0001-02 - remove-duplicates-from-an-unsorted-linked-list - #c++.cpp"
	print("come-3")
	filepath = ""
	filepath += str(object.problem_id.id).zfill(4) + '-'
	filepath += str(object.id).zfill(2) + ' - '
	filepath += object.problem_id.slug + ' - '
	# here is we know that one solution have only one programming language, so there is simple...
	plObject = ProgrammingLanguages.objects.get(id=SolutionsProgrammingLanguage)
	filepath += "#" + plObject.name.lower()
	filepath += plObject.extension
	print(f"<{object.filename}>")
	print("come-4")
	return filepath