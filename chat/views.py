from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'chat/room.html', context)

def main(request):
    return render(request, 'chat/main.html')

def logoutView(request):
    logout(request)
    return redirect('/')
