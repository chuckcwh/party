from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from partyApp.forms import ProfileForm, UserImageForm, UserEditForm


def index(request):
    return render(request, 'index.html')

@login_required
def user(request):
    # if 'img' in request.POST and request.method == 'POST':
    #     imageform = UserImageForm(request.POST, request.FILES, instance=request.user)
    #     if imageform.is_valid():
    #         imageform.save()
    # elif 'data' in request.POST and request.method == 'POST':
    #     editform = UserEditForm(request.POST, instance=request.user)
    #     if editform.is_valid():
    #         editform.save()
    # else:
    #     imageform = UserImageForm()
    #     editform = UserEditForm()

    if request.method == 'POST':
        print request.POST
        imageform = UserImageForm(request.POST, request.FILES, instance=request.user)
        if imageform.is_valid():
            imageform.save()
    else:
        imageform = UserImageForm()

    if request.method == 'POST':
        editform = UserEditForm(request.POST, instance=request.user)
        if editform.is_valid():
            editform.save()
    else:
        editform = UserEditForm()

    return render(request, 'user.html', {
        'imageform': imageform,
        'editform': editform
    })

def event(request):
    return render(request, 'event.html')


def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
    else:
        form = ProfileForm()

    return render(request, "registration/register.html", {
        'form': form,
    })