from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),

		# aur-all-apps-dummy-collections : we activate this till the app not haven...
		path('edittables/',views.edittables,name='edittables'),
		path('codesubmissions/',views.codesubmissions,name='codesubmissions'),
		path('problemsubmissions/',views.problemsubmissions,name='problemsubmissions'),


		# path('problems/new/',views.addproblems,name='addproblems'),
		# path('solutions/new/',views.addsolutions,name='addsolutions'),
		# path('problemsandsolutions/new/',views.addproblemsandsolutions,name='addproblemsandsolutions'),

		# path('problems/edit/',views.editproblems,name='editproblems'),
		# path('solutions/edit/',views.editsolutions,name='editsolutions'),

		# path('problems/wholelist/',views.problemswholelist,name='problemswholelist'),
		# path('problemsandsolutions/',views.openproblemsandsolutions,name='openproblemsandsolutions'),





		path('problem/new/',views.addProblem,name='addProblem'),
		path('solution/new/<slug:problemslug>/',views.addSolution,name='addSolution'),
		path('problem-solution/new/',views.addProblemAndSolution,name='addProblemAndSolution'),

		path('problem/edit/<slug:problemslug>/',views.editProblem,name='editProblem'),
		path('solution/edit/<slug:problemslug>/<str:solutionid>/',views.editSolution,name='editSolution'),

		path('problem/onlyproblems/',views.problemsOnly,name='problemsOnly'),
		path('problem/wholelist/',views.problemsWholeList,name='problemsWholeList'),
		path('problem-solution/<slug:problemslug>/<str:solutionid>/',views.ProblemWithSolution,name='ProblemWithSolution'),

		# here is showing problem, and other solutions
		path('problem/<slug:problemslug>/',views.openProblem,name='openProblem'),


]


