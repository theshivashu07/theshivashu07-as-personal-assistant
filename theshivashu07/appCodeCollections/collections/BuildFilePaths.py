

from appCodeCollections.models import *
# import appCodeCollections.models as MODELs
import appCodeCollections.collections._default as DEFAULTs





def assignProblem(object,ProblemsDataStructures,wholeStatement):
	# lets create files for problem-input.
	object.filename = buildProblemFilePath(object,ProblemsDataStructures)
	object.save()  #must to save this, so that it also save on the main place.
	with open( f"{DEFAULTs.problems_location}\\{object.filename}" , 'wb' ) as file: 
		# actually below we converting normal-text-data to a binary-data.
		file.write(wholeStatement.encode("ascii",errors="xmlcharrefreplace"))
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
		object.detailsset=file.read().decode("ascii",errors="xmlcharrefreplace")
		object.detailsset =  '<br>'.join( object.detailsset.split('\n') )
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
	# wents like ---> "0001-01 - remove-duplicates-from-an-unsorted-linked-list - #python.py"
	filepath = str(object.problem_id.id).zfill(4) + '-'
	filepath += str(object.id).zfill(2) + ' - '
	filepath += object.problem_id.slug + ' - '
	# here is we know that one solution have only one programming language, so there is simple...
	plObject = ProgrammingLanguages.objects.get(id=SolutionsProgrammingLanguage)
	filepath += "#" + plObject.name.lower()
	filepath += plObject.extension
	return filepath



