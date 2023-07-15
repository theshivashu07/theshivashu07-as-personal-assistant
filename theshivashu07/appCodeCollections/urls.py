from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),

		# aur-all-apps-dummy-collections : we activate this till the app not haven...
		path('edittables/',views.edittables,name='edittables'),
		path('codesubmissions/',views.codesubmissions,name='codesubmissions'),
		path('problemsubmissions/',views.problemsubmissions,name='problemsubmissions'),

		path('problems/new/',views.addproblems,name='addproblems'),
		path('solutions/new/',views.addsolutions,name='addsolutions'),
		path('problemsandsolutions/new/',views.addproblemsandsolutions,name='addproblemsandsolutions'),

		path('problems/edit/',views.editproblems,name='editproblems'),
		path('solutions/edit/',views.editsolutions,name='editsolutions'),

		path('problems/wholelist/',views.problemswholelist,name='problemswholelist'),
		path('problemsandsolutions/',views.openproblemsandsolutions,name='openproblemsandsolutions'),

		# path('justtry/',views.justtry,name='justtry'),
		# path('/codecollections/',views.problemsubmissions,name='problemsubmissions'),


		# path('index/',views.index,name='index'),
]


