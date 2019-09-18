from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show

def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {
        "show_list" : Show.objects.all()
    }
    return render(request, 'tv_shows_app/all_shows.html', context)

def show_new(request):
    return render(request, 'tv_shows_app/add_shows.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('shows/new')

    else: 
        show_title = request.POST['title']
        show_network = request.POST['network_name']
        show_date = request.POST['release_date']
        show_description = request.POST['show_desc']
        Show.objects.create(title=show_title, network=show_network, release_date= show_date, desc=show_description)
        show= Show.objects.get(title = show_title)
        show_id = show.id
        return redirect(f'shows/{show_id}')

def display(request, show_id):
    context = {
        "show_info" : Show.objects.get(id = show_id) 
    }
    return render(request, 'tv_shows_app/display_shows.html', context)

def edit(request, show_id):
    show = Show.objects.get(id = show_id)
    context = {
        "show_info" : Show.objects.get(id = show_id),
        "release_date" : show.release_date.strftime("%Y-%m-%d"),
        "show_id" : show_id
    }
    return render(request, 'tv_shows_app/edit.html', context)

def update(request, show_id):
    update_show = Show.objects.get(id = show_id)
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f'/shows/{show_id}/edit')
    
    if len(request.POST['title']) != 0 and update_show.title !=  request.POST['title']:
        update_show.title = request.POST['title']
        update_show.save()
    if len(request.POST['network_name']) != 0 and update_show.network != request.POST['network_name']:
        update_show.network = request.POST['network_name']
        update_show.save()
    if len(request.POST['release_date']) != 0 and update_show.release_date != request.POST['release_date']:
        update_show.release_date = request.POST['release_date']
        update_show.save()
    if len(request.POST['show_desc']) != 0 and update_show.desc != request.POST['show_desc']:
        update_show.desc = request.POST['show_desc']
        update_show.save()
    return redirect(f'/shows/{show_id}')

def destroy(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')

# Create your views here.
