from shop.forms import SingUpForm, UpdateForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import CustomUser


def register_request(request):
    form = SingUpForm()

    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for', user)
            return redirect('')
        else:
            messages.warning(request, form.errors)

    context = {'form': form}
    return render(request, template_name="accounts/signup.html", context=context)


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('hhh')
            messages.error(request, 'Email or password incorrect')
            return redirect('login')
    return render(request, template_name="accounts/login.html")


def account(request, pk, *args, **kwargs):
    cuser = CustomUser.objects.get(id=pk)
    order = cuser.order_set.filter(complete=True)

    form = UpdateForm()

    if request.method == "POST":
        user = CustomUser.objects.get(id=pk)
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            print('hhh')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was update for', user)
            return redirect('')
        else:
            print(form.errors)

    context = {
        'user': cuser,
        'order': order,
        'form': form,
        # 'shipping': shipping,
    }
    return render(request, 'accounts/my-account.html', context)

def update_request(request, pk):
    form = UpdateForm()

    if request.method == "POST":
        user = CustomUser.objects.get(id=pk)
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            print('hhh')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was update for', user)
            return redirect('account',pk)
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, template_name="accounts/my-account.html", context=context)


def logoutUser(request):
    logout(request)
    return redirect('home')
