from django.shortcuts import HttpResponse, render, redirect
from .models import User, UserManager, Password, PasswordManager
from django.contrib import messages

# PAGES
def index(request):
    return render(request, "first_app/login.html")

def process_new(request):
    return render(request, "first_app/register.html")

def password_dashboard(request):
    the_user = User.objects.get(id=request.session['id'])
    all_passwords = the_user.my_passwords.all()

    print(all_passwords)
    print(the_user.first_name)

    context = {
        'passwords': all_passwords,
        'user': the_user
    }

    return render(request, "first_app/dashboard.html", context)

def add_password(request):
    the_user = User.objects.get(id=request.session['id'])

    print(the_user.id)
    return render(request, "first_app/add_password.html")

# LOGIN, REG, LOGOUT
def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    if request.POST['password'] == request.POST['confirm_password']:
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        print('User Created')

        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        print(new_user.id)

        return redirect('/password_dashboard')

    else:
        print('Passwords did not match')
        return redirect('/register_page')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])

    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0]. first_name
            request.session['id'] = logged_user[0]. id

            return redirect('/password_dashboard')
    
    else:
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

# ADD PASSWORDS
def password_added(request):
    if 'user' in request.session:
        the_user = User.objects.get(id=request.session['id'])
        errors = Password.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_password')
        
        else: 
            new_password = Password.objects.create(company=request.POST['company'], email=request.POST['email'], password=request.POST['password'], the_user=the_user)
            print('Password Added To: ', the_user.first_name)
            print('New Password: ', new_password.company)
            return redirect('/password_dashboard')

def delete(request, password_id):
    the_password = Password.objects.get(id=password_id)
    the_password.delete()

    return redirect('/password_dashboard')

def edit(request, password_id):
    the_user = User.objects.get(id=request.session['id'])
    password = Password.objects.get(id = password_id)

    print(password)
    print(the_user.first_name)

    context = {
        'password': password,
    }

    return render(request, "first_app/edit_password.html", context)

def on_edit_pass(request, password_id):
    the_password = Password.objects.get(id = password_id)

    the_password.company = request.POST['company']
    the_password.email = request.POST['email']
    the_password.password = request.POST['password']
    the_password.save()

    return redirect("/password_dashboard")

def profile(request):
    the_user = User.objects.get(id=request.session['id'])

    print(the_user.first_name)

    context = {
        'user': the_user
    }

    return render(request, "first_app/edit_profile.html", context)

def on_edit_user(request, user_id):
    the_user = User.objects.get(id = user_id)

    if request.POST['password'] == request.POST['confirm_password']:
        the_user.first_name = request.POST['first_name']
        the_user.last_name = request.POST['last_name']
        the_user.email = request.POST['email']
        the_user.password = request.POST['password']
        the_user.save()
    else:
        return redirect("/profile")

    return redirect("/password_dashboard")

def mobile_display(request, password_id):
    the_password = Password.objects.get(id = password_id)

    print(the_password)

    context = {
        'password': the_password,
    }
    
    return render(request, "first_app/mobile_display.html", context)

