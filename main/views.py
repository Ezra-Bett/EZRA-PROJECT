from django.shortcuts import render, redirect

from . forms import CreateUserForm

from . forms import LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import ProfileUpdateForm
from .models import Profile

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def services_index(request):
    return render(request, 'services_index.html')

def about_index(request):
    return render(request, 'about_index.html')



# def homepage(request):
     

#      pass

def register(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
              form.save()
              return redirect('main:login')
        
    context = {'registerform': form}


    return render(request, 'register.html', context)



def login(request):

         form = LoginForm()
         context = {'loginForm': form}
         if request.method == 'POST':
               form = LoginForm(request, data=request.POST)
               if form.is_valid():
                     username = request.POST.get('username')
                     password = request.POST.get('password')

                     user = authenticate(request, username=username, password=password)

                     if user is not None:
                           Profile.objects.get_or_create(user=user)

                           auth.login(request, user)

                           return redirect('main:dashboard')
                     
                     else:
                        messages.error(request, "Incorrect username or password")                        

         context = {'loginForm':form}


         return render(request, 'login.html', context)


def logout(request):
      auth.logout(request)
      return redirect("")



@login_required(login_url="main:login")
def dashboard(request):
          return render(request, 'dashboard.html')


def profile(request):
      return render(request, 'profile.html')


def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('main:profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }

    return render(request, 'profile.html', context)


# password_reset_logic


# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.contrib import messages

# def password_reset_request(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         users = User.objects.filter(email=email)
#         if users.exists():
#             for user in users:
#                 uid = urlsafe_base64_encode(force_bytes(user.pk))
#                 token = default_token_generator.make_token(user)
#                 reset_url = request.build_absolute_uri(
#                     reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
#                 )
#                 # Send the reset email
#                 send_mail(
#                     subject="Password Reset Request",
#                     message=f"Click the link to reset your password: {'password_reset'}",
#                     from_email="ezrab@gmail.com",
#                     recipient_list=[email],
#                 )
#             messages.success(request, "A password reset link has been sent to your email.")
#             return redirect('password_reset_done')
#         else:
#             messages.error(request, "No account found with that email address.")
    
#     return render(request, 'password_reset_form.html')

# # main/views.py
# def password_reset_done(request):
#     return render(request, 'password_reset_done.html')


# # main/views.py
# from django.contrib.auth import update_session_auth_hash

# def password_reset_confirm(request, uidb64, token):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64)).decode()
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         if request.method == "POST":
#             new_password = request.POST.get("password")
#             confirm_password = request.POST.get("confirm_password")

#             if new_password == confirm_password:
#                 user.set_password(new_password)
#                 user.save()
#                 update_session_auth_hash(request, user)  # Keeps the user logged in after password change
#                 messages.success(request, "Your password has been reset successfully.")
#                 return redirect('password_reset_complete')
#             else:
#                 messages.error(request, "Passwords do not match.")
#         return render(request, 'password_reset_confirm.html')
#     else:
#         messages.error(request, "The password reset link is invalid.")
#         return redirect('password_reset')


# # main/views.py
# def password_reset_complete(request):
#     return render(request, 'password_reset_complete.html')
