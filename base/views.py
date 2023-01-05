from django.shortcuts import render,redirect
from . models import Message, Project,Photo
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # projects = Project.objects.all()
    p = Paginator(Project.objects.all(),6)
    page = request.GET.get('page')
    projects = p.get_page(page)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')

        Message.objects.create(name=name,email=email,body=body)
        return redirect('home')
    context = {'projects':projects}
    return render(request,'base/home.html',context)

def photoPage(request):
    photos = Photo.objects.all()
    print(photos)
    count = [1,2,3,4,5,6]
    context = {'photos':photos,'count':count}
    return render(request,'base/photo-page.html',context)