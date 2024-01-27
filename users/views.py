from django.shortcuts import render, redirect
from django.contrib import messages # flash message. The message is displayed once and will dissapear on the next request
from django.contrib.auth.forms import UserCreationForm # Django way (Class) of creating the registration form 

# Create your views here.
def register (request):
    if request.method == 'POST':  # Form is submitted as a post request
        form = UserCreationForm(request.POST)  # Create a new form that has the data in the post. 'Username and two password fields'
        if form.is_valid():  # Check multiple django conditions like, does the user exist? Do the passwords match? If invalid, it returns the render
            form.save()  # Save the user
            username = form.cleaned_data.get('username')  # Grab the username
            messages.success(request, f'Account created for {username}!')  # Our flash message
            return redirect ('blog-home')  # Note the absence of render
    else:
        form = UserCreationForm()
    return render (request, 'users/register.html', {'form': form})  # Render our register.html document with a form

'''

Types of messages:
message.debug
message.info
message.success
message.warning
message.error

'''