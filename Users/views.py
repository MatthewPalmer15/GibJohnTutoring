from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import user_creation_form, user_change_password, user_change_details
from django.contrib.auth import get_user_model
from Courses.models import Award

# Gets User Database that is used within the other functions
user_db = get_user_model()

# Function to allow the user to log into their account
def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                if not user_db.objects.filter(username=username):
                    return render(request, 'users/login.html', {"error_message":"The username you have entered is incorrect. Please try again"})
                else:
                    return render(request, 'users/login.html', {"error_message":"The password you have entered is incorrect. Please try again"})
                    
        else:
            return render(request, 'users/login.html', {})


# Function to allow the user to log out of their account
def user_logout(request):
    logout(request=request)
    return redirect('index')


# Function to allow the user to register a new account
def user_register(request):
    if request.method == "POST":
        form = user_creation_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, 'users/register.html', {"form":form}) 
    else:
        form = user_creation_form()
        print(form.errors)
    return render(request, 'users/register.html', {"form":form})   


# Function to allow the user to change their details
def user_details_change(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == 'POST':
        form = user_change_details(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_view')
    else:
        form = user_change_details(instance=request.user)
    return render(request, 'users/change_details.html', {"form":form})   


# Function to allow the user to change their password
def user_password_change(request):
    if not request.user.is_authenticated:
        return redirect("login")
        
    if request.method == 'POST':
        form = user_change_password(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user_view')
        else:
            print(form.errors)
    else:
        form = user_change_password(user=request.user)
    return render(request, 'users/change_password.html', {"form":form})   


# Function to allow the user to see the account details of their account
def user_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        all_user_awards = Award.objects.filter(user_id=request.user)
        gold_awards = all_user_awards.filter(trophy="gold").count()
        silver_awards = all_user_awards.filter(trophy="silver").count()
        bronze_awards = all_user_awards.filter(trophy="bronze").count()
        recent_awards = all_user_awards.order_by("-completion_date")[:10]
        return render(request, 'users/view.html', {
            "awards":recent_awards,
            "gold_awards": gold_awards,
            "silver_awards": silver_awards,
            "bronze_awards": bronze_awards,
        })


# Function to allow the user to delete their account
def user_delete(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        current_user = user_db.objects.filter(username=request.user.username)
        current_user.delete()
        return redirect('index')