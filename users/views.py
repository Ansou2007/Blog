from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def connexion(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('article_list')
        
        else:
            messages.error(request,'Login ou mot de passe incorrecte')
            return redirect('login')


    return render(request,'login.html')


# Deconnexion
def deconnexion(request):
    logout(request)
    return redirect('login')