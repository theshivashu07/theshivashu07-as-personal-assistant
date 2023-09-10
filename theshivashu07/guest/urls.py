from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),

		# aur-all-apps-dummy-collections : we activate this till the app not haven...
		path('profile/',views.profile_metaverse,name='profile_metaverse'),
		path('studycenter/',views.study_center,name='study_center'),
		# path('codecollections/',views.code_collections,name='code_collections'),
		path('dailyroutines/',views.daily_routines,name='daily_routines'),
		path('enjoysections/',views.enjoy_sections,name='enjoy_sections'),

		# this section if for test any code...
		path('defaultsections/',views.default_sections,name='default_sections'), 

		# path('index/',views.index,name='index'),




]


