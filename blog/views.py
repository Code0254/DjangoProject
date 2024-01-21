from django.shortcuts import render
from .models import Post # imports the database into the view

'''
# Dummy Data
posts =[
    {
        'author' : 'Brian K',
        'title' : 'Blog post 1',
        'Content': 'Our first post',
        'date_posted' : '09 January 2024'

    },
    {
        'author' : 'Vanessa M',
        'title' : 'Blog post 2',
        'Content': 'Our second post',
        'date_posted' : '09 February 2024'
    }
]
'''
# Create your views here.

def home (request): #  we will handle the request argument later
    context= {
        'posts': Post.objects.all() # updated from 'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about (request): #  we will handle the request argument later
    return render(request , 'blog/about.html', {'title': 'About'} ) 