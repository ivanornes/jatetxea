from django.shortcuts import render_to_response, get_object_or_404
from menus.models import Menu
from django.http import HttpResponse

def index(request):
    latest_menu_list = Menu.objects.all().order_by('-fecha')[:5]
    return render_to_response('menus/index.html', {'latest_menu_list': latest_menu_list})

def detail(request, menu_id):
    p = get_object_or_404(Menu, pk=menu_id)
    return render_to_response('menus/detail.html', {'menu': p})

def results(request, menu_id):
    return HttpResponse("You're looking at the results of poll %s." % menu_id)

def vote(request, menu_id):
    return HttpResponse("You're voting on poll %s." % menu_id)