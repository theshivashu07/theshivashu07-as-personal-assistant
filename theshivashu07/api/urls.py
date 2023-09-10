from django.urls import path
from . import views


urlpatterns=[
		# path('',views.index,name='index'),

		#testing-api
		path('problem/<int:id>',views.problem,name='problem'),
		path('problems/',views.problems,name='problems'),


]


