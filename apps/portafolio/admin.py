from django.contrib import admin
from .models import Category, ProjectTechnology, Project, ProjectMedia

admin.site.register(Category)
admin.site.register(ProjectTechnology)
admin.site.register(Project)
admin.site.register(ProjectMedia)