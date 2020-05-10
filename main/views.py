from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import slider , postrequest ,city
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    sliders = slider.objects.all()
    n = len(sliders)
    city = postrequest.objects.values('city')
    if request.method == 'POST':
        cit = request.POST.get('location','')
        content = postrequest.objects.filter(city=cit)
        all = {'sliders': sliders , 'city': city, 'content': content }
        return render(request, 'main/index.html', all)
    else:
        all = {'sliders': sliders, 'city': city}
    return render(request,'main/index.html', all)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/events/accounts/login/')
def post(request):
    if request.method=="POST":
        title = request.POST.get('title', '')
        category = request.POST.get('category', '')
        address = request.POST.get('address', '')
        cityo = request.POST.get('city', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        poster = request.POST.get('poster', '')
        desc = request.POST.get('description','')
        posts = postrequest(title=title, category=category, address=address, date=date, time=time, poster=poster, desc=desc, verification=False)
        #instance = posts.save(commit=False)
        posts.author = request.user
        posts.city = city.objects.get(location=cityo)
        posts.save()
    return render(request, 'main/post.html')
class postevent(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'

def links(request):
    return HttpResponse("This is links")

def places(request):
    return HttpResponse("This is Places")

def maulana(request):
    return HttpResponse("This is maulana")