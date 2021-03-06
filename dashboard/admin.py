from django.contrib import admin
from .models import *

# Register your models here.

class MealInLine(admin.TabularInline):
    model = Meal

class TimeAdmin(admin.ModelAdmin):
    inlines = [MealInLine,]

class TimeInLine(admin.TabularInline):
    model = Time

class SuggestionInLine(admin.TabularInline):
    model = Suggestion

class PlaceAdmin(admin.ModelAdmin):
    inlines = [TimeInLine,SuggestionInLine]

admin.site.register(Place, PlaceAdmin)
admin.site.register(Time,TimeAdmin)
admin.site.register(Meal)




