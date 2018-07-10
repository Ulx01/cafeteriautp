from django.http import HttpResponse
from django.template import loader
from .models import Time, Place, Meal


def index(request):
    places = Place.objects.all()
    template = loader.get_template('dashboard\index.html')
    context = {'cafeterias':places}
    return HttpResponse(template.render(context,request))
# Create your views here.

def place(request, place_id):
    p = Place.objects.get(pk = place_id)#obtiene la cafeteria por su ID
    times = Time.objects.filter(place = p)#obtiene los turnos de comidas correspondientes a la cafeteria
    meals  = Meal.objects.all()#obtiene todas las comidas
    template = loader.get_template('dashboard\place.html')
    context = {'turnos':times,'cafeteria':p,'comida':meals}
    return HttpResponse(template.render(context,request))


'''def get_menus_recomendation(meal_period, meal_list):
    recomendatios = []
    pk = 1
    for time in meal_period:
        for meal in meal_list:'''

