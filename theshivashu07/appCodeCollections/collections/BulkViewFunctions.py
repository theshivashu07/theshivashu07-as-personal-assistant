

from appCodeCollections.models import *
import appCodeCollections.collections.BuildFilePaths as BuildFilePaths




def ProblemDataSet(problemID):
	object=Problems.objects.get(id=problemID.id)
	holds=problems_plateforms.objects.filter(problem_id=problemID.id)
	object.plateforms=[ Plateforms.objects.get(pk=object.plateform_id) for object in holds ]
	holds=problems_datastructures.objects.filter(problem_id=problemID.id)
	object.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]
	holds=problems_dsasheetlist.objects.filter(problem_id=problemID.id)
	object.dsasheetlist=[ DSAsSheetsLists.objects.get(pk=object.dsasheetlist_id) for object in holds ]
	object.subproblem = SubProblems.objects.filter(problem_id=problemID.id)

	# problem-assignment - and there is getting problem-file's data!!!
	BuildFilePaths.getProblem(object)

	return object


def SolutionDataSet(problemID,solutionID):
	object=Solutions.objects.get(id=solutionID)
	object.programminglanguages=ProgrammingLanguages.objects.get(pk=object.programminglanguages)
	holds=solutions_datastructures.objects.filter(solution_id=solutionID)
	object.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ] 
	object.attachments = SolutionsAttachments.objects.filter(solution_id=solutionID)

	# solution-assignment - and there is getting solution-file's data!!!
	BuildFilePaths.getSolution(object)

	return object





def AddProblems(request):
	# when you want to ADD Problems...
	ProblemsTitle=request.POST["ProblemsTitle"]
	ProblemsPlateforms=request.POST.getlist("ProblemsPlateforms")
	ProblemsDataStructures=request.POST.getlist("ProblemsDataStructures")
	ProblemsDSAsSheetsLists=request.POST.getlist("ProblemsDSAsSheetsLists")
	ProblemsDetailSet=request.POST["ProblemsDetailSet"]
	ProblemsTimeComplexity=request.POST["ProblemsTimeComplexity"]
	ProblemsAuxiliarySpace=request.POST["ProblemsAuxiliarySpace"]

	# object = Problems.objects.get(pk=problemID.id)  
	object = Problems()

	if(ProblemsTitle):
		object.title=ProblemsTitle
		object.save()

	if(ProblemsPlateforms):
		object.plateforms=len(ProblemsPlateforms)
		holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=object.id) ]
		for id in ProblemsPlateforms:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_plateforms()
				miniobject.problem_id=object
				miniobject.plateform_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_plateforms.objects.get(plateform_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(ProblemsDataStructures):
		object.datastructures=len(ProblemsDataStructures)
		holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=object.id) ]
		for id in ProblemsDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_datastructures()
				miniobject.problem_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_datastructures.objects.get(datastructure_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(ProblemsDSAsSheetsLists):
		object.dsasheetlist=len(ProblemsDSAsSheetsLists)
		holds = [ str(object.dsasheetlist_id) for object in problems_dsasheetlist.objects.filter(problem_id=object.id) ]
		for id in ProblemsDSAsSheetsLists:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_dsasheetlist()
				miniobject.problem_id=object
				miniobject.dsasheetlist_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_dsasheetlist.objects.get(dsasheetlist_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(ProblemsDetailSet):
		object.detailsset=ProblemsDetailSet
		object.save()

	if(ProblemsTimeComplexity):
		object.timecomplexity=ProblemsTimeComplexity
		object.save()

	if(ProblemsAuxiliarySpace):
		object.auxiliaryspace=ProblemsAuxiliarySpace
		object.save()

	# problem-assignment - and there is build file with its name!!!
	BuildFilePaths.assignProblem(object,ProblemsDataStructures,ProblemsDetailSet)

	return object
	# return None



def EditProblems(request,problemID):
	# when you want to EDIT Problems...
	ProblemsTitle=request.POST["ProblemsTitle"]
	ProblemsPlateforms=request.POST.getlist("ProblemsPlateforms")
	ProblemsDataStructures=request.POST.getlist("ProblemsDataStructures")
	ProblemsDSAsSheetsLists=request.POST.getlist("ProblemsDSAsSheetsLists")
	ProblemsDetailSet=request.POST["ProblemsDetailSet"]
	ProblemsTimeComplexity=request.POST["ProblemsTimeComplexity"]
	ProblemsAuxiliarySpace=request.POST["ProblemsAuxiliarySpace"]

	object = Problems.objects.get(pk=problemID.id)  
	# object = Problems()

	if(ProblemsTitle):
		object.title=ProblemsTitle
		object.save()

	if(ProblemsPlateforms):
		object.plateforms=len(ProblemsPlateforms)
		holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=object.id) ]
		for id in ProblemsPlateforms:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_plateforms()
				miniobject.problem_id=object
				miniobject.plateform_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_plateforms.objects.get(plateform_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()
				
	if(ProblemsDataStructures):
		object.datastructures=len(ProblemsDataStructures)
		holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=object.id) ]
		for id in ProblemsDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_datastructures()
				miniobject.problem_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_datastructures.objects.get(datastructure_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(ProblemsDSAsSheetsLists):
		object.dsasheetlist=len(ProblemsDSAsSheetsLists)
		holds = [ str(object.dsasheetlist_id) for object in problems_dsasheetlist.objects.filter(problem_id=object.id) ]
		for id in ProblemsDSAsSheetsLists:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_dsasheetlist()
				miniobject.problem_id=object
				miniobject.dsasheetlist_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_dsasheetlist.objects.get(dsasheetlist_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(ProblemsDetailSet):
		object.detailsset=ProblemsDetailSet
		object.save()

	if(ProblemsTimeComplexity):
		object.timecomplexity=ProblemsTimeComplexity
		object.save()

	if(ProblemsAuxiliarySpace):
		object.auxiliaryspace=ProblemsAuxiliarySpace
		object.save()

	# problem-assignment - and there is build file with its name!!!
	BuildFilePaths.assignProblem(object,ProblemsDataStructures,ProblemsDetailSet)

	return object
	# return None


def AddSolutions(request,problemID):
	# when you want to ADD Solution...
	SolutionsLink=request.POST["SolutionsLink"]
	SolutionsNote=request.POST["SolutionsNote"]
	SolutionsShownTitle=request.POST["SolutionsShownTitle"]
	SolutionsDataStructures=request.POST.getlist("SolutionsDataStructures")
	SolutionsProgrammingLanguage=request.POST["SolutionsProgrammingLanguage"]
	SolutionsTimeComplexity=request.POST["SolutionsTimeComplexity"]
	SolutionsAuxiliarySpace=request.POST["SolutionsAuxiliarySpace"]
	SolutionsCodeSubmissions=request.POST["SolutionsCodeSubmissions"]

	object=Solutions()
	# object=Solutions.objects.get(pk=1) 

	object.problem_id=problemID
	object.codesubmissions=SolutionsCodeSubmissions
	object.save()

	if(SolutionsProgrammingLanguage):
		object.programminglanguages=SolutionsProgrammingLanguage
		object.save()

	# if(SolutionsPlateforms):
	# 	object.plateforms=SolutionsPlateforms
	# 	object.save()

	if(SolutionsTimeComplexity):
		object.timecomplexity=SolutionsTimeComplexity
		object.save()

	if(SolutionsAuxiliarySpace):
		object.auxiliaryspace=SolutionsAuxiliarySpace
		object.save()

	# must that you putted any one data-structure...
	if(SolutionsDataStructures):
		object.datastructures=len(SolutionsDataStructures)
		holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
		for id in SolutionsDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=solutions_datastructures()
				miniobject.solution_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = solutions_datastructures.objects.get(datastructure_id=id, solution_id=object.id)
				miniobject.delete()
		object.save()

	# must that you putted any one data-structure...
	if(SolutionsLink or SolutionsShownTitle or SolutionsNote):
		object.attachments=1
		object.save()
		tempobject = SolutionsAttachments()
		tempobject.solution_id = object
		tempobject.link = SolutionsLink
		tempobject.note = SolutionsNote
		tempobject.showntitle = SolutionsShownTitle
		tempobject.save()

	# solution-assignment - and there is build file with its name!!!
	BuildFilePaths.assignSolution(object,SolutionsProgrammingLanguage,SolutionsCodeSubmissions)

	# add-SolutionsCount
	problemID.SolutionsCount += 1
	problemID.save()

	return object
	# return None


def EditSolutions(request,problemID,solutionID):
	# when you want to EDIT Solution...
	SolutionsLink=request.POST["SolutionsLink"]
	SolutionsNote=request.POST["SolutionsNote"]
	SolutionsShownTitle=request.POST["SolutionsShownTitle"]
	SolutionsDataStructures=request.POST.getlist("SolutionsDataStructures")
	SolutionsProgrammingLanguage=request.POST["SolutionsProgrammingLanguage"]
	# SolutionsPlateforms=request.POST["SolutionsPlateforms"]
	SolutionsTimeComplexity=request.POST["SolutionsTimeComplexity"]
	SolutionsAuxiliarySpace=request.POST["SolutionsAuxiliarySpace"]
	SolutionsCodeSubmissions=request.POST["SolutionsCodeSubmissions"]

	# object=Solutions()
	object=Solutions.objects.get(id=solutionID) 

	object.problem_id=problemID
	object.codesubmissions=SolutionsCodeSubmissions
	object.save()

	if(SolutionsProgrammingLanguage):
		object.programminglanguages=SolutionsProgrammingLanguage
		object.save()

	# must that you putted any one data-structure...
	if(SolutionsLink or SolutionsShownTitle or SolutionsNote):
		tempobjects = SolutionsAttachments.objects.filter(solution_id=solutionID)
		object.attachments=len(tempobjects)
		object.save()
		tempobject = tempobjects[0]
		tempobject.solution_id = object
		tempobject.link = SolutionsLink
		tempobject.note = SolutionsNote
		tempobject.showntitle = SolutionsShownTitle
		tempobject.save() 

	if(SolutionsTimeComplexity):
		object.timecomplexity=SolutionsTimeComplexity
		object.save()

	if(SolutionsAuxiliarySpace):
		object.auxiliaryspace=SolutionsAuxiliarySpace
		object.save()

	# must that you putted any one data-structure...
	if(SolutionsDataStructures):
		object.datastructures=len(SolutionsDataStructures)
		holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
		for id in SolutionsDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=solutions_datastructures()
				miniobject.solution_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = solutions_datastructures.objects.get(datastructure_id=id, solution_id=object.id)
				miniobject.delete()
		object.save()

	# solution-assignment - and there is build file with its name!!!
	BuildFilePaths.assignSolution(object,SolutionsProgrammingLanguage,SolutionsCodeSubmissions)

	return object
	# return None











def AllProblemWithOrWithoutSolutions(incoming):
	def findSolutionObjects(id):
		templist = list()
		for object in Solutions.objects.all():
			if(object.problem_id.id==id):
				object.programminglanguages = ProgrammingLanguages.objects.get(id=object.programminglanguages).name
				templist.append(object)
		return templist

	returnback = dict()
	for object in Problems.objects.all():
		tracks = { '__all__':True, '__with__':bool(object.SolutionsCount), '__without__':not bool(object.SolutionsCount) }
		if tracks[incoming]:
			solutionsobject = findSolutionObjects(object.id)
			returnback[object] = solutionsobject
	return returnback













def getBaseStructure():
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'DSAsSheetsLists' : DSAsSheetsLists.objects.all(),
	}
	return thisisReturningDatabase


def getbackProblemDetails(request):
	''' This situations comes when we go to submit new problem, and problem is not good!!! '''
	thisisReturningDatabase = {
		'ProblemDataSet' : {
			'title' : request.POST["ProblemsTitle"],
			'plateforms' : [ Plateforms.objects.get(id=id) for id in request.POST.getlist("ProblemsPlateforms") ],
			'datastructures' : [ DataStructures.objects.get(id=id) for id in request.POST.getlist("ProblemsDataStructures") ],
			'detailsset' : request.POST["ProblemsDetailSet"],
			'timecomplexity' : request.POST["ProblemsTimeComplexity"],
			'auxiliaryspace' : request.POST["ProblemsAuxiliarySpace"],
		}
	}
	return thisisReturningDatabase


def getbackSolutionDetails(request):
	''' This situations comes when we go to submit new solution, and solution is not good!!! '''
	thisisReturningDatabase = {
		'SolutionDataSet' : {
			'datastructures' : [ DataStructures.objects.get(id=id) for id in request.POST.getlist("SolutionsDataStructures") ],
			# 'programminglanguages' :  request.POST.getlist("SolutionsProgrammingLanguage"),
			'programminglanguages' :  ProgrammingLanguages.objects.get( id=request.POST["SolutionsProgrammingLanguage"] ),
			'timecomplexity' : request.POST["SolutionsTimeComplexity"],
			'auxiliaryspace' : request.POST["SolutionsAuxiliarySpace"],
			'codesubmissions' : request.POST["SolutionsCodeSubmissions"],
		}
	}
	print(thisisReturningDatabase)
	return thisisReturningDatabase







