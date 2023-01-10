from django.shortcuts import render,redirect
from project_management_app.forms import ProjectRegistrationForm,TaskRegistrationForm,ProjectTypeForm
from .models import Project,Task
# Create your views here.

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return redirect("project_management_app:projects")
        else:
            return render(request, 'new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'new_project.html', context)

def projectsView(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'projects_view.html', context)

def projectUpdateView(request, id):
    objects = Project.objects.get(id=id)
    tasks=Task.objects.filter(project_id=id)
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("project_management_app:projects")
    else:
        form = ProjectRegistrationForm(instance=objects)

    return render(request,"project_update.html",{'form': form,"objects":objects,"tasks":tasks})

def projectDelete(request, id):
  project_object = Project.objects.get(id=id)
  project_object.delete()
  return redirect("project_management_app:projects")

def ProjectTypeView(request):
    if request.method == 'POST':
        form = ProjectTypeForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'project_type.html', context)
        else:
            return render(request, 'project_type.html', context)
    else:
        form = ProjectTypeForm()
        context = {
            'form': form,
        }
        return render(request,'project_type.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return redirect("project_management_app:project")
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'new_task.html', context)

def taskView(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks,
    }
    return render(request, 'tasks_view.html', context)        

def taskUpdateView(request, id):
    objects = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("project_management_app:tasks")
    else:
        form = TaskRegistrationForm(instance=objects)

    return render(request,"task_update.html",{'form': form ,"objects":objects})    

def taskDelete(request, id):
  project_object = Task.objects.get(id=id)
  project_object.delete()
  return redirect("project_management_app:tasks")