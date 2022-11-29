from django.shortcuts import render
from .models import Profile, user
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from rest_framework.views import APIView
from .serializer import UserSerializer


#class LoginView(APIView):
def user_login(request,email):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user_details = {}
                    user_details['username'] = "%s %s" % (
                    user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                    return HttpResponse('Authenticated successfully', user_details)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})

from .forms import LoginForm, UserRegistrationForm
from rest_framework.permissions import AllowAny

def register(request):
    if request.method == 'POST':
        #user_form = UserRegistrationForm(request.POST)
        permission_classes = (AllowAny,)
        serializer_class = UserSerializer
        data = request.POST
        serializer = UserSerializer(data=data) 
        serializer.is_valid(raise_exception=True)
        user_form = UserRegistrationForm(request.POST)
        #permission_classes = (AllowAny,)
        #serializer_class = RegistrationSerializer
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            #new_user.request.data.get('email')
            # Set the chosen password
            #new_user=self.model(username=username, email=self.normalize_email(email))
            new_user.set_password(user_form.cleaned_data['password'])
            #data.set_password(user_form.cleaned_data['password'])
            #data.cleaned_data['password']
            # Save the User object
            #new_user.set_email(user_form.cleaned_data['email'])
            #new_user.save()
            serializer.save()
            
            return render(request, 'register_done.html', {'new_user': serializer})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                      'edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

