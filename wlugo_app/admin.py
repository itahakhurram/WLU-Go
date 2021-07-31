from django.contrib import admin
from .models import Rating
#from .models import Course

class ratingAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'code', 'name', 'description', 'department','rating_id','score','mean_grade')
    
#class courseAdmin(admin.ModelAdmin):
    #list_display = ('rating_id', 'birdness','usefulness','enjoyability')


# Register your models here.
admin.site.register(Rating)
#admin.site.course(Course, courseAdmin)
