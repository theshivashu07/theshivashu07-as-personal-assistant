

from rest_framework import serializers

class ProblemsSerializer(serializers.Serializer):
	id = serializers.IntegerField();
	title = serializers.CharField(max_length=100);
	filename = serializers.CharField(max_length=150); 
	slug = serializers.CharField(max_length=100);
	plateforms = serializers.IntegerField();
	links = serializers.IntegerField();
	datastructures = serializers.IntegerField();
	dsasheetlist = serializers.IntegerField();
	subproblem = serializers.IntegerField();
	# detailsset = serializers.IntegerField();
	detailsset = serializers.CharField(max_length=500); 
	timecomplexity = serializers.CharField(max_length=35);
	auxiliaryspace = serializers.CharField(max_length=35);
	SolutionsCount = serializers.IntegerField();   # It indicates, this problem's how much solutions are here right now???
	SolutionsContinueCount = serializers.IntegerField();  # It indicates, this problem's how much solution's we push till now, deleted+existing.
	JoiningDate = serializers.DateTimeField();
	UpdationDate = serializers.DateTimeField(); 














