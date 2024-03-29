from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm, 'error':_('This username is already in use. Please choose another one')})
            except ValueError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm, 'error':_('Incorrect data has been entered ')})
        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm, 'error':_('Passwords are a mismatch')})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm,'error':_("Username and password don't match")})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            if newtodo.due_date and newtodo.due_date < timezone.now():
                raise ValueError
            if newtodo.notify_date and newtodo.due_date:
                if newtodo.notify_date < timezone.now():
                    raise ValueError
                else:
                    during_time = newtodo.notify_date - timezone.now()
                    during_time = int(during_time.total_seconds() * 1000)
                    request.session["title"] = _("The due date is close at hand!")
                    request.session["body"] = _("Todo ") + '"' + newtodo.title + '"' + _(" is about to expire!")
                    request.session["during_time"] = during_time
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
                return render(request, 'todo/createtodo.html', {'form':TodoForm, 'error':_('Incorrect data has been entered ')})


@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True).order_by('-datecompleted')
    for todo in todos:
        if todo.due_date and timezone.now() > todo.due_date:
            todo.datecompleted = todo.due_date
            todo.save()
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True).order_by('-datecompleted')
    if 'during_time' in request.session:
        during_time = request.session['during_time']
        del request.session['during_time']
    else:
        during_time = 0
    return render(request, 'todo/currenttodos.html',{'todos':todos, "during_time": during_time})


@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'todo/completedtodos.html',{'todos':todos})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html',{'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                notify_date = form.cleaned_data["notify_date"]
                due_date = form.cleaned_data["due_date"]
                title = form.cleaned_data["title"]
                if due_date and due_date < timezone.now():
                    raise ValueError
                if notify_date and due_date:
                    if notify_date < timezone.now():
                        raise ValueError
                    else:
                        during_time = notify_date - timezone.now()
                        during_time = int(during_time.total_seconds() * 1000)
                        request.session["title"] = _("The due date is close at hand!")
                        request.session["body"] = _("Todo ") + '"' + title + '"' + _(" is about to expire!")
                        request.session["during_time"] = during_time   
                form.save()
                return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html',{'todo':todo, 'form':form, 'error':_('Incorrect data has been entered ')})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')
