from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth
from datetime import datetime
from .models import Contact
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as user_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from home.models import Tour, Tag, Program, Gallary, Subject, Profile, Register, TourBooking

# Create your views here.
#All pages Links.
# razorpay_client = razorpay.Client(
#     auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def index(request):
    return render(request, "index.html",{})

def About(request):
    return render(request, "about.html",{})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('registerFirstName')
        last_name = request.POST.get('registerLastName')
        email = request.POST.get('registerEmail')
        username = request.POST.get('registerUsername')
        password = request.POST.get('registerPassword')
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username is already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': 'Email is already use'})

        # Create the user
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            # user_login(self.request, user):
            user_login(request,user)
            if user.is_superuser:
                # Redirect superuser to admin panel
                return redirect('/admin/')
            return redirect('index')  # Redirect to the home page after successful login
        else:
            return render(request, "login.html", {'error_message': 'Invalid username or password'})
    return render(request, "login.html")

def profile(request):
    return render(request, 'profile.html')

def thankyou(request):
    return render(request, 'thankyou.html')


@login_required
def profile(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        image = request.FILES.get('image_up_lode')
        email = request.POST.get('email')
        # dob = request.POST.get('d_o_b')
        # Update User model
        user = User.objects.get(username=request.user.username)
        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        user.email = email
        user.save()

        # Update or create Profile instance
        profile_instance, created = Profile.objects.get_or_create(user=request.user)
        print(image)
        if image:
            profile_instance.profile_picture = image
        profile_instance.save()
        return redirect('index')
    # contex of profile page
    context = {
    }
    return render(request, 'profile.html',context)

def Logout(request):
    logout(request)
    return redirect('login')


def Booking(request):
    return render(request, "booking.html",{})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        # return redirect('contact')
        contact.save()
        return redirect('contact')
    return render(request, "contact.html",{})

def faq(request):
    return render(request, "faq.html",{})

def testimonial(request):
    return render(request, "testimonial-page.html",{})

def packages(request):

    tour = Tour.objects.all()

    return render(request, "packages.html", context={'tour' : tour})

def Packages(request, slug):

    tour = Tour.objects.get(slug = slug)
    context = {
        "tour" : tour
    }
    return render(request, "package-detail.html", context=context)


def booking(request):
    if request.method == 'POST':
        firstname_booking = request.POST.get('firstname_booking')
        lastname_booking = request.POST.get('lastname_booking')
        email_booking = request.POST.get('email_booking')
        phone_number = request.POST.get('phone_number')
        firstname_card = request.POST.get('firstname_card')
        card_number = request.POST.get('card_number')
        expire_month = request.POST.get('expire_month')
        expire_year = request.POST.get('expire_year')
        ccv = request.POST.get('ccv')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username is already taken'})

        booking = TourBooking(firstname_booking=firstname_booking, lastname_booking=lastname_booking,
                          email_booking=email_booking, phone_number=phone_number,
                          firstname_card=firstname_card, card_number=card_number,
                          expire_month=expire_month, expire_year=expire_year,
                          ccv=ccv, date=datetime.today())
        booking.save()
    return render(request, 'register.html',{})
