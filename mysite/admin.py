from django.contrib import admin
from mysite import models

class StoryAdmin(admin.ModelAdmin):
	list_display=('sno','contrib')
		

admin.site.register(models.Story)
# Register your models here.
