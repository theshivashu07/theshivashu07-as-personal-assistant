
from appCodeCollections.models import DataStructures,Plateforms,ProgrammingLanguages,DSAsSheetsLists

# Instructions : To call that function only write two lines!!!
	# we use below lines to get dummy data
	# import dummyFunction as dummy 
	# dummy.function()


# this functions is helping us to add all dummy data directly, without to manually submissions
def function(request=None):

	import json
	file = open('dummyData.json')
	DATAs = json.load(file)

	tracks = { 'DataStructures':DataStructures(), 'Plateforms':Plateforms(), 'ProgrammingLanguages':ProgrammingLanguages(), 'DSAsSheetsLists':DSAsSheetsLists() }

	for data in DATAs['DataStructures']:
		object = DataStructures()
		object.name = data['name']
		object.slug = data['slug']
		object.save()
	for data in DATAs['Plateforms']:
		object = Plateforms()
		object.name = data['name']
		object.slug = data['slug']
		object.color = data['color']
		object.bgcolor = data['bgcolor']
		object.save()
	for data in DATAs['ProgrammingLanguages']:
		object = ProgrammingLanguages()
		object.name = data['name']
		object.slug = data['slug']
		object.extension = data['extension']
		object.save()
	for data in DATAs['DSAsSheetsLists']:
		object = DSAsSheetsLists()
		object.name = data['name']
		object.slug = data['slug']
		object.by = data['by']
		object.reference = data['reference']
		object.save()
	return None


