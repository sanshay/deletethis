from django.shortcuts import render,redirect

def index(request):
    if request.user.is_authenticated:
        
        return render(request,'chat/chat.html',{})
    else:
        a=redirect('login')
        return a