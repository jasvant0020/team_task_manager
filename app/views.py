from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import Task, Project, User
from django.db.models import Count

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


from django.contrib.auth.decorators import login_required
from .models import Project

from django.utils.timezone import now

@login_required
def dashboard(request):
    projects = request.user.projects.all()

    tasks = Task.objects.filter(project__in=projects)

    total_tasks = tasks.count()
    todo = tasks.filter(status="TODO").count()
    in_progress = tasks.filter(status="IN_PROGRESS").count()
    done = tasks.filter(status="DONE").count()

    overdue = tasks.filter(
        due_date__lt=now().date(),
        status__in=["TODO", "IN_PROGRESS"]
    ).count()

    #  NEW: Tasks per user
    tasks_per_user = tasks.values("assigned_to__username").annotate(count=Count("id"))

    return render(request, "dashboard.html", {
        "projects": projects,
        "total_tasks": total_tasks,
        "todo": todo,
        "in_progress": in_progress,
        "done": done,
        "overdue": overdue,
        "tasks_per_user": tasks_per_user,
    })

@login_required
def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        project = Project.objects.create(
            name=name,
            description=description,
            created_by=request.user
        )

        project.members.add(request.user)  # creator becomes member

        return redirect("dashboard")

    return render(request, "create_project.html")

@login_required
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)

    #  Restrict access
    if request.user not in project.members.all():
        return redirect("dashboard")

    tasks = project.tasks.all()

    #  Members see only their tasks
    if request.user.role == "MEMBER":
        tasks = tasks.filter(assigned_to=request.user)

    return render(request, "project_detail.html", {
        "project": project,
        "tasks": tasks
    })

from .models import Task, Project, User

@login_required
def create_task(request, project_id):
    project = Project.objects.get(id=project_id)

    #  Only admin
    if request.user.role != "ADMIN":
        return redirect("dashboard")

    users = project.members.all()

    if request.method == "POST":
        assigned_user = User.objects.get(id=request.POST.get("assigned_to"))

        #  Ensure user is part of project
        if assigned_user not in project.members.all():
            return redirect("project_detail", project_id=project.id)

        Task.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            due_date=request.POST.get("due_date"),
            priority=request.POST.get("priority"),
            project=project,
            assigned_to=assigned_user
        )

        return redirect("project_detail", project_id=project.id)

    return render(request, "create_task.html", {
        "project": project,
        "users": users
    })

@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    #  Must belong to project
    if request.user not in task.project.members.all():
        return redirect("dashboard")

    #  ONLY assigned user can update
    if task.assigned_to != request.user:
        return redirect("dashboard")

    if request.method == "POST":
        task.status = request.POST.get("status")
        task.save()
        return redirect("project_detail", project_id=task.project.id)

    return render(request, "update_task.html", {"task": task})

@login_required
def manage_members(request, project_id):
    project = Project.objects.get(id=project_id)

    #  Only admin (project creator)
    if request.user != project.created_by:
        return redirect("dashboard")

    users = User.objects.exclude(id=request.user.id)

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        action = request.POST.get("action")

        user = User.objects.get(id=user_id)

        #  FIXED PART
        if action == "add":
            if user not in project.members.all():
                project.members.add(user)

        elif action == "remove":
            if user in project.members.all():
                project.members.remove(user)

        return redirect("manage_members", project_id=project.id)

    return render(request, "manage_members.html", {
        "project": project,
        "users": users
    })