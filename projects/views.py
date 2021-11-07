from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project

from .forms import ProjectForm


def home(request):
    return render(request, 'projects/index.html')


def projects(request):
    projectObj = Project.objects.all()
    context = {'projects': projectObj}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/info-form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    context = {}
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    template = 'projects/info-form.html'

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context['form'] = form

    return render(request, template, context)


@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete.html', {'object': project})


# def project2(request, pk):
#     return render(request, 'projects/contacts.html')


# def project3(request, pk):
#     return render(request, 'projects/login.html')


# def project4(request, pk):
#     return render(request, 'projects/doctors.html')


# def project5(request, pk):
#     return render(request, 'projects/hospitals.html')


# def project6(request, pk):
#     return render(request, 'projects/appointmnet.html')


# def project7(request, pk):
#     return render(request, 'projects/ambulance.html')
