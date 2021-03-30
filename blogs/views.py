from django.shortcuts import render, HttpResponse
from .models import blogposts,contacts
# Create your views here.
def index(request):
    posts = blogposts.objects.all()
    return render(request, 'blogs/index.html', {'posts':posts})

def about(request):
    return render(request, 'blogs/about.html')

def contact(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Message=request.POST['message']
        if(len(Name)>0 and len(Email)>0 and len(Message)>0):
            tobesave = contacts(Name = Name, Email=Email,Message = Message)
            tobesave.save()

            thank = True
            return render(request, 'blogs/contact.html', {'thank': thank})

        else:
            thank = False
            return render(request, 'blogs/contact.html', {'thank': thank})
    return render(request, 'blogs/contact.html')

def search(request):
    query = request.GET['query']
    posts1 = blogposts.objects.filter(Title__icontains= query)
    posts2 = blogposts.objects.filter(Subtitle__icontains= query)
    posts3 = blogposts.objects.filter(Post__icontains= query)
    postsA = posts1.union(posts2)
    posts = postsA.union(posts3)
    params = {'posts': posts, 'query': query}
    # posts={'allPosts': allPosts}
    return render(request, 'blogs/search.html', params)

