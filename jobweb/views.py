from django.contrib.auth import authenticate, login
from distutils.command.upload import upload
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from jobweb.models import Register
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse("This is homepage")


def about(request):
    return render(request, 'about.html')


def details(request):
    return render(request, 'details.html')


def services(request):
    return render(request, 'services.html')


def login1(request):
    return render(request, 'login1.html')

def home2(request):
    return render(request, 'home2.html')


def loguser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "home2.html", {'username': username})
        else:
            messages.error(request, "Invalid password or username. Please try again")
            return redirect('loguser')

    return render(request, 'loguser.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name1 = request.POST.get('fname')
        name2 = request.POST.get('lname')
        contact = request.POST.get('cont')
        jobs = request.POST.get('jobs')
        city = request.POST.get('city')
        org = request.POST.get('org')
        year = request.POST.get('year1')
        ep = request.POST.get('ep')
        link = request.POST.get('link')
        # doc = request.FILES['doc']
        # fs = FileSystemStorage()
        # fs.save(doc.name,doc)
        reg = Register(email=email, first_name=name1, last_name=name2, contact_number=contact,
                            Applying_for_Expertise=jobs, city_or_location=city, current_or_last_organization=org,
                            Years_of_experience=year,LinkedIn_Profile_Page_URL=link,EP_no=ep)
        reg.save()

    return render(request, 'register.html')

def register1(request):
    if request.method == 'POST':
    #   fname = request.POST['fname']
    #   lname = request.POST['lname']
      email = request.POST.get('email')
      username = request.POST['username']
      pass1 = request.POST['pass1']

      myuser = User.objects.create_user(username, email, pass1)
    #   myuser.first_name = fname 
    #   myuser.last_name = lname
      myuser.save()
      return redirect('loguser')

    return render(request, 'register1.html')