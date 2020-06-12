from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import slider , postrequest ,city , Shaiyar, contact
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import Nameform,details , UserAdminCreationForm, mehfilform
from .decorators import unauthenticated_user, allowed_users

def index(request):
    sliders = slider.objects.all()
    n = len(sliders)
    cityy = city.objects.all().order_by('location')
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
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserAdminCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/events/accounts/login/')
#@unauthenticated_user
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
        return render(request, 'main/thanks.html')
        #send_mail('Post Form',title,settings.EMAIL_HOST_USER,['hussainimeraj5@gmail.com'],fail_silently=False)
    return render(request, 'main/post.html')
class postevent(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'

def eventdetail(request,post_id):
    eventdetail=postrequest.objects.filter(post_id=post_id)
    return render(request,'main/eventdetail.html',{'eventdetail':eventdetail[0]})

def postmore(request):
    if request.method == "POST":
        sname = request.POST.get('sname')
        imag = request.POST.get('si')
        qwe = Shaiyar(Shaiyarname=sname, photo=imag)
        qwe.post = postrequest.objects.get(post_id=19)
        qwe.save()
    return render(request, 'main/postmore.html')
def links(request):
    n=4
    return render(request, 'main/links.html',{'n':range(n)})

def places(request):
    n=2
    return render(request,'main/places.html', {'n':range(n),'y':range(6)})

def maulana(request):
    return HttpResponse("This is maulana")

def contactt(request):
    if request.method == 'POST':
        form1 = details(request.POST,request.FILES)
        form2 = mehfilform(request.POST)
        print(form1)
        print(form2)
        if form1.is_valid() and form2.is_valid():
            #meh=form1.save(mehfil)
            obj = mehfildetail()
            obj.nizamat = form1.cleaned_data['nizamat']
            obj.nizamimage = request.FILES['nizamimag']
            obj.sadarat = form1.cleaned_data['sadarat']
            obj.sadaratimag = request.FILES['sadaratimag']
            #obj.contacter = form.cleaned_data['your_name']
            obj.mehfil = postrequest(82)
            #add.mehfil = meh
            obj.save()
            return HttpResponse("Submit")
    else:
        form1 = details()
        form2 = mehfilform()
    return render(request, 'main/name.html',locals())

@unauthenticated_user
@allowed_users(allowed_roles=['volunteer'])
def volunteer(request):
    majlis = postrequest.objects.filter(category='majlis')
    mehfil = postrequest.objects.filter(category='mehfil')
    others = postrequest.objects.filter(category='others')
    unverified = postrequest.objects.filter(verification='False')
    all = {'majlis': majlis, 'mehfil':mehfil, 'others':others, 'unverified': unverified}
    return render(request, 'main/volunteer.html', all)

@login_required
def home(request):
    return render(request, 'main/home.html')
