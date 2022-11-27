from django.shortcuts import render
from shop.forms import SingUpForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_request(request):
    form = SingUpForm()

    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for', user)
            return redirect('login')
        else:
            print(form.errors)

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
            messages.error(request, 'Username or password incorrect')
            return redirect('login')
    return render(request, template_name="accounts/login.html" )


def logoutUser(request):
    logout(request)
    return redirect('login')