from django.shortcuts import render



posts = [
    {
        'author': 'Dotun',
        'title': 'The jouney',
        'content': 'The start is a step to greatness',
        'date_posted': '02 June,2019',
    }
]

def home(request) :
    context = {
        'posts': posts,
    }
    return render(request, 'blogapp/home.html', context)



def about(request) :
    return render(request, 'blogapp/about.html', {'title' : 'About Page'})
