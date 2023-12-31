from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),

		# aur-all-apps-dummy-collections : we activate this till the app not haven...
		path('edit-tables/',views.edittables,name='edittables'),


		# when want to add new problem or its solution or both, so we use these urls!!!
		path('add-problem/',views.addProblem,name='addProblem'),
		path('add-solution/<slug:problemslug>/',views.addSolution,name='addSolution'),
		# path('add-problem-solution/',views.addProblemAndSolution,name='addProblemAndSolution'),

		# when wanted to update/edit our problems or solutions, we call these solutions!!!
		path('edit-problem/<slug:problemslug>/',views.editProblem,name='editProblem'),
		path('edit-solution/<slug:problemslug>/<str:solutionid>/',views.editSolution,name='editSolution'),

		# when want to delete any problem or its solution or both, so we use these urls!!!
		path('delete-problem/<slug:problemslug>/',views.deleteProblem,name='deleteProblem'),
		path('delete-solution/<slug:problemslug>/<str:solutionid>/',views.deleteSolution,name='deleteSolution'),

		path('add-problem-links/<slug:problemslug>/',views.addProblemsLinks,name='addProblemsLinks'),
		path('add-solution-attachments/<slug:problemslug>/<str:solutionid>/',views.addSolutionsAttachments,name='addSolutionsAttachments'),

		# these are two specific urls, first is all problem with solution, and second is problems which solution not available!!!
		path('problems-with-solutions/',views.fatchProblemsWithOrWithoutSolutions,name='fatchProblemsWithOrWithoutSolutions'),
		path('problems-without-solutions/',views.fatchProblemsWithOrWithoutSolutions,name='fatchProblemsWithOrWithoutSolutions'),		
		path('problems-with-or-without-solutions/',views.fatchProblemsWithOrWithoutSolutions,name='fatchProblemsWithOrWithoutSolutions'),

		path('problems/',views.allProblemsLists,name='allProblemsLists'),

		# here is showing problem, and other solutions only links available, not all solutions shows!!!
		path('problem/<slug:problemslug>/',views.openProblem,name='openProblem'),

		# when we want to show problem with any specific solutions, so we use this!!!
		path('problem-solution/<slug:problemslug>/<str:solutionid>/',views.ProblemWithSolution,name='ProblemWithSolution'),


		# this is completly vella-testing-page, if any new future coming in our mind, we test this here...
		path('testing-page/',views.openTestingPage,name='openTestingPage'),

]

# 
