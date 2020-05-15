from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import slider , postrequest ,city , Shaiyar
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
    cityy = city.objects.values('location','id')
    print(cityy)
    if request.method == 'POST':
        cit = request.POST.get('locationn')
        print(cit)
        content = postrequest.objects.filter(place=cit)
        all = {'sliders': sliders , 'cityy': cityy, 'content': content }
        return render(request, 'main/index.html', all)
    else:
        all = {'sliders': sliders, 'cityy': cityy}
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
        cityo = request.POST.get('cityyy', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        poster = request.POST.get('poster', '')
        desc = request.POST.get('description','')
        sname = request.POST.get('sname')
        imag = request.POST.get('si')
        posts = postrequest(title=title, category=category, address=address, date=date, time=time, poster=poster, desc=desc, verification=False)
        posts.author = request.user
        posts.place = city.objects.get(location=cityo)
        posts.save()
        if(posts.category=='mehfil'):
            qwe = Shaiyar(Shaiyarname=sname, photo=imag)
            qwe.post = postrequest.objects.get(post_id=posts.post_id)
            qwe.save()

    return render(request, 'main/post.html')
class postevent(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'

def postmore(request):
    if request.method == "POST":
        sname = request.POST.get('sname')
        imag = request.POST.get('si')
        qwe = Shaiyar(Shaiyarname=sname, photo=imag)
        qwe.post = postrequest.objects.get(post_id=19)
        qwe.save()
    return render(request, 'main/postmore.html')
def links(request):
    return HttpResponse("This is links")

def places(request):
    return HttpResponse("This is Places")

def maulana(request):
    return HttpResponse("This is maulana")