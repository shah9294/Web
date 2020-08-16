from django.shortcuts import render
# Create your views here.


posts = [
    {
        'author':'shah',
        'title':'Blog Post 1',
        'content':"First Post Comment",
        'date_posted':'August 27 2018'
    },
    {
        'author':'hamza',
        'title':'Blog Post 2',
        'content':"Second Post Comment",
        'date_posted':'Sept 27 2018'
    }
]


def home(request):
    context={
        "posts":posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':"About"})
    