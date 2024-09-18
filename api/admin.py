from django.contrib import admin
from .models import Meal,Rating,Profile
# Register your models here.
# 1
class MealAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_display_links = ['title','description']

admin.site.register(Meal,MealAdmin)

# 2
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','meal','user','stars']
    list_display_links = ['meal','user','stars']
    
admin.site.register(Rating,RatingAdmin)

# 3
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','image','user','age']
    list_display_links = ['id','image','user','age']
    
admin.site.register(Profile,ProfileAdmin)