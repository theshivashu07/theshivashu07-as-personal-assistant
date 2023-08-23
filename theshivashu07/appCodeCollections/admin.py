from django.contrib import admin
# Register your models here.
from .models import DataStructures,Plateforms,ProgrammingLanguages,DSAsSheetsLists
from .models import Problems, problems_plateforms, problems_datastructures, problems_dsasheetlist, problems_links, SubProblems
from .models import Solutions, solutions_datastructures, SolutionsAttachments, SolutionAndSolutionsAttachments





admin.site.register(DataStructures)
admin.site.register(Plateforms)
admin.site.register(ProgrammingLanguages)
admin.site.register(DSAsSheetsLists)

admin.site.register(Problems)
admin.site.register(problems_plateforms)
admin.site.register(problems_datastructures)
admin.site.register(problems_dsasheetlist)
admin.site.register(problems_links)
admin.site.register(SubProblems)

admin.site.register(Solutions)
admin.site.register(solutions_datastructures)
admin.site.register(SolutionsAttachments)
admin.site.register(SolutionAndSolutionsAttachments)








