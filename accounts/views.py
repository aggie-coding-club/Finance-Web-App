from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
  if request.method == 'GET':
    return render(request, 'register.html', {'messages': []})
  elif request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    print(request.POST)

    messages = []
    
    # Check if username is taken
    if User.objects.filter(username=username):
      messages.append('Username not available.')

    # Check if passwords match
    if password1 != password2:
      messages.append('Passwords do not match.')
    
    if messages:
      return render(request, 'register.html', {'messages': messages})
    else:
      user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password1
      )
      user.save()
      print('User created.')
      return redirect('/')