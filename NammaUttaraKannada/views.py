from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'GALLERY.html')


def contact(request):
    return render(request, 'CONTACT.html')


def signin(request):
    if request.method == "POST":
        username = request.POST["userName"]
        passwd = request.POST["password"]

        user = authenticate(username=username, password=passwd)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signin')

    return render(request, 'sign_in.html')


def signup(request):
    if request.method == "POST":
        username = request.POST["userName"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username):
            return redirect('signup')
        if User.objects.filter(email=email):
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password)

        myuser.save()

        return render(request, 'sign_in.html')

    return render(request, 'sign_up.html')


def book(request):
    if request.method == 'POST':
        dest = request.POST['destname']
        mail = request.POST['mail']
        datefrom = request.POST['dateFrom']
        dateto = request.POST['dateTo']
        rooms = request.POST['room']
        adult = request.POST['adults']
        child = request.POST['child']

        html_content = render_to_string('eTemplate.html',
                                        {'dest': dest,
                                         'datefrom': datefrom,
                                         'dateto': dateto,
                                         'rooms': rooms,
                                         'adult': adult,
                                         'child': child
                                         })
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Your Request Has Submitted",
            text_content,
            settings.EMAIL_HOST_USER,
            ['sourabhrk360@gmail.com', mail]
        )

        email.attach_alternative(html_content, "text/html")
        email.send()
        return redirect('index')

    return render(request, 'book.html')
