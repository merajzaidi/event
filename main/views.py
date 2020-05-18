from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import slider , postrequest ,city , Shaiyar, contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import Nameform,details
from .decorators import unauthenticated_user, allowed_users
def index(request):
    sliders = slider.objects.all()
    n = len(sliders)
    cityy = city.objects.values('location','id')
    print(cityy)
    if request.method == 'POST':
        cit = request.POST.get('locationn')
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

#@login_required(login_url='/events/accounts/login/')
@unauthenticated_user
def post(request):
    form = details()
    if request.method=="POST":
        title = request.POST.get('title', '')
        category = request.POST.get('category', '')
        address = request.POST.get('address', '')
        cityo = request.POST.get('cityyy', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        poster = request.POST.get('poster', '')
        desc = request.POST.get('description','')
        attend = request.POST.get('attendences','')
        organisers = request.POST.get('organiser','')
        phone_no = request.POST.get('phone_no','')
        posts = postrequest(title=title, category=category, address=address, date=date, time=time, poster=poster, desc=desc, verification=False, attendences = attend, organiser = organisers,phone_no=phone_no)
        posts.author = request.user
        posts.place = city.objects.get(location=cityo)
        posts.save()
        i = 1
        if(posts.category=='mehfil'):
            sname = request.POST.get('sname'+str(i), '')
            imag = request.POST.get('si'+str(i), '')
            while(sname != ''):
                qwe = Shaiyar(Shaiyarname=sname, photo=imag)
                qwe.post = postrequest.objects.get(post_id=posts.post_id)
                qwe.save()
                i=i+1
                sname = request.POST.get('sname' + str(i), '')
                imag = request.POST.get('si' + str(i), '')


    return render(request, 'main/post.html',{'form':form})
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

def contactt(request):
    if request.method == 'POST':
        form = Nameform(request.POST)
        print(form)
        if form.is_valid():
            obj = contact()
            obj.contacter = form.cleaned_data['your_name']
            obj.save()
            return HttpResponse("Submit")
    else:
        form=Nameform()
    return render(request, 'main/name.html',{'form':form})

@unauthenticated_user
@allowed_users(allowed_roles=['volunteer'])
def volunteer(request):
    majlis = postrequest.objects.filter(category='majlis')
    mehfil = postrequest.objects.filter(category='mehfil')
    others = postrequest.objects.filter(category='others')
    unverified = postrequest.objects.filter(verification='False')
    all = {'majlis': majlis, 'mehfil':mehfil, 'others':others, 'unverified': unverified}
    return render(request, 'main/volunteer.html', all)