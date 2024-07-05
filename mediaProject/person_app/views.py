from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person


def add_person(request):
    template_name = 'person_app/person_form.html'
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/v1/person-list/')
    return render(request, template_name, context={'form': form})


def show_persons(request):
    template_name = 'person_app/person_list.html'
    queryset = Person.objects.all()
    return render(request, template_name, context={'objects_list': queryset})


def update_person(request, pk=None):
    template_name = 'person_app/person_form.html'
    object = Person.objects.get(pk=pk)
    form = PersonForm(instance=object)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('/v1/person-list/')
    return render(request, template_name, context={'form': form})
