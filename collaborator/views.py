# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Collaborator, Project, Value, Role, Task, Category, Concept, ConceptCategory, ExplorationDate, Candidacy
from django.contrib.auth.decorators import login_required
from .forms import CategoryFilterForm, ProjectForm
from datetime import date, timedelta

def home(request):
    user = request.user
    return render(request, 'collaborator/home.html', locals())

@login_required
def profile(request):
    collab = request.user.collaborator
    return render(request, 'collaborator/profile.html', locals())

@login_required
def organizational_chart(request):
    company = request.user.collaborator.company
    return render(request, 'collaborator/orga_chart.html', locals())

@login_required
def development_modules(request):
    collab = request.user.collaborator
    recents = ExplorationDate.objects.filter(collaborator=collab, date__gte=date.today()-timedelta(days=5))
    categories = ConceptCategory.objects.all()
    return render(request, 'collaborator/dev_mods.html', locals())

@login_required
def collective_initiative(request):
    collab = request.user.collaborator
    return render(request, 'collaborator/my_projects.html', locals())

@login_required
def other_projects(request):
    form = CategoryFilterForm(request.GET or None)
    if form.is_valid():
        print('coucou')
        print(form.cleaned_data)
        selected_categories = []
        for category in Category.objects.all():
            if form.cleaned_data['category'+str(category.id)]:
                selected_categories += [category]
        if len(selected_categories) == 0:
            projects_whithout = Project.objects.exclude(id__in=[project.id for project in request.user.collaborator.projects.all()])
        else:
            proj_ids = []
            for category in selected_categories:
                for project in category.contains.all():
                    if not project.id in proj_ids:
                        proj_ids += [project.id]
        projects_whithout = Project.objects.exclude(id__in=[project.id for project in request.user.collaborator.projects.all()]).filter(id__in = proj_ids)    
    return render(request, 'collaborator/other_projects.html', locals())

@login_required
def new_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            new_project = Project.objects.create(name=name, description=description)
            new_project.save()
            new_role = Role.objects.create(project=new_project, collaborator=request.user.collaborator, role_name='chef de projet')
            new_role.save()
            categories = Category.objects.all()
            for category in categories:
                if form.cleaned_data['category'+str(category.id)]:
                    category.contains.add(new_project)
            return redirect('collec_init')
    return render(request, 'collaborator/new_project.html', locals())

@login_required
def my_project(request, project_id=1):
    project = Project.objects.get(id=project_id)
    if not(request.user.collaborator in project.members.all()):
        return redirect('other_project', project_id)
    else:
        values = Value.objects.all()
        roles = Role.objects.filter(project=project)
        other_members = Collaborator.objects.exclude(user__in = [member.user for member in project.members.all()])
        if request.method=='POST':
            project.description = request.POST['new_desc']
            project.save()
        return render(request, 'collaborator/my_project.html', locals())

@login_required
def other_project(request, project_id=1):
    project = Project.objects.get(id=project_id)
    if request.user.collaborator in project.members.all():
        return redirect('my_project', project_id)
    else:
        free_roles = Role.objects.filter(project=project, collaborator__isnull=True)
        if request.method == 'POST':
            role = Role.objects.get(id=request.POST['wanted_role'])
            new_candidacy = Candidacy.objects.create(role=role, collaborator=request.user.collaborator, description=request.POST['description'])
            new_candidacy.save()
        return render(request, 'collaborator/other_project.html', locals())
        
@login_required
def change_values(request, project_id=1):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        for value in Value.objects.all():
            if str(value.id) in request.POST.keys():
                project.values.add(value)
            else:
                project.values.remove(value)
        project.save()
    return redirect('my_project', project_id)

@login_required
def ask_money(request, project_id=1):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        print("requête envoyée")
        print(request.POST['budget'])
    return redirect('my_project', project_id)

@login_required
def show_member(request, role_id=1):
    role = Role.objects.get(id=role_id)
    tasks = Task.objects.filter(role=role)
    all_roles = Role.objects.filter(collaborator=role.collaborator)
    all_tasks = Task.objects.filter(role__in=all_roles)
    return render(request, 'collaborator/show_member.html', locals())
    
@login_required
def chatbot(request):
    return redirect('home')

@login_required
def barometers(request):
    return redirect('home')

@login_required
def help(request):
    return redirect('home')
