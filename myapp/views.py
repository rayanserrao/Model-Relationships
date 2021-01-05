from django.shortcuts import render
from django.contrib.auth.models import User
from myapp.models import Page,Post,Song

# Create your views here.
def home(request):
    return render(request,'home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2= User.objects.filter(email = 'rayan@gmail.com')
    data3 = User.objects.filter(username = 'rahul')
    data4 = User.objects.filter(page__page_cat='python')
    data5 = User.objects.filter(post__pots_publish_date='2021-01-07')
    data6= User.objects.filter(song__song_dur=5)
    return render(request,'user.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6,})

def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat='python')
    data3 = Page.objects.filter(user__email='rayan@gmail.com')
    return render(request,'page.html',{'data1':data1,'data2':data2,'data3':data3})

def show_post_data(request):
    data1= Post.objects.all()
    data2 = Post.objects.filter(post_cat = 'python')
    data3 = Post.objects.filter(user__email='rayan@gmail.com')
    return render(request,'post.html',{'data1':data1,'data2':data2,'data3':data3})

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_dur=5)
    data3 = Song.objects.filter(user__username ='rahul')
    return render(request,'song.html',{'data1':data1,'data2':data2,'data3':data3})