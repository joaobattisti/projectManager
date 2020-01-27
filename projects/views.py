from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

from activities.models import Activity

# Create your views here.
@login_required
def list_project(request):
    projects = Project.objects.all()
    activity = Activity.objects.all()
    return render(request, "projects.html", {'projects': projects, 'activity': activity})

@login_required
def new_project(request):
    form = ProjectForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('list_project')
    return render(request, 'new_project.html', {'form': form})

@login_required
def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('list_project')

    return render(request, 'new_project.html', {'form': form})

@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == 'POST':
        project.delete()
        return redirect('list_project')

    return render(request, 'project_delete.html', {'project': project})
