from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Music 
from .models.music import Music
from .models.category import Category
from .models.watchlater import Watchlater
from .models.channel import Channel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Case,When

from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    musics = Music.objects.all()
    
     
    categories=Category.objects.all()
    categoryId=request.GET.get('category')
    
    
    if categoryId:
        musics=Music.get_by_id(categoryId)
    else:
        musics=Music.objects.all()
        
    
    
    params = {'music': musics, 'range': range(len(musics)),'categories':categories}
    return render(request, 'songs/index.html', params)

# def cats(request,id):
#     # category = request.GET.get('category')
#     cat=Category.objects.filter(id=id)
#     print(cat,"hii")
#     prod=Music.objects.filter(id=Category)
#     print(prod)
#     return render(request,'songs/cat.html',{'cat':cat,'id':id})
    
def play(request, id):
    # song=Music.objects.filter(music_id=id).first()
    musics = Music.objects.filter(id=id).first()
    return render(request, 'songs/playsong.html', {'music': musics, 'id': id})

def home(request):
    return render(request,'songs/home.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username,password=pass1)
        from django.contrib.auth import login
        login(request,user)
        redirect("/songs")
        
    return render(request,'songs/login.html')
def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.name=name
        
        myuser.save()
        user=authenticate(username=username,password=pass1)
        from django.contrib.auth import login
        
        login(request,user)
        
        channel=Channel(name=username)
        channel.save()
        
        return redirect('/songs')
    return render(request,'songs/signup.html')

def watchlater(request):
    if request.method=="POST":
        user=request.user
        video_id=request.POST['video_id']
        
        watch=Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id==i.video_id:
                message="Your music is already in watchlater"
                break
        else:
            watchlater=Watchlater(user=user,video_id=video_id)
            watchlater.save()
            message="successfully added"
        
        song=Music.objects.filter(id=video_id).first()
        # return render(request,f"songs/",{'song':song,'message':message})
        return redirect(f"/songs/{video_id}")
    
    categories=Category.objects.all()
    wl=Watchlater.objects.filter(user=request.user)
    ids=[]
    for i in wl:
        ids.append(i.video_id)
    
    preserved=Case(*[When(pk=pk,then=pos) for pos,pk  in enumerate(ids)])
    song=Music.objects.filter(id__in=ids).order_by(preserved)
    
    return render (request,'songs/watchlater.html',{'song':song,'categories':categories})

# def watchlater(request):
#     if request.method=="POST":
#         user=request.user
#         video_id=request.POST['video_id']
        
#         # watch=Watchlater.objects.filter(user=user)
        
#         # for i in watch:
#         #     if video_id==i.video_id:
#         #         message="Your music is already in watchlater"
#         #         break
#         # else:
#         watchlater=Watchlater(user=user,video_id=video_id)
#         watchlater.save()
#         message="successfully added"
        
#         # song=Music.objects.filter(id=video_id).first()
#         return redirect(f"/songs/{video_id}")
    
  
    
#     return render (request,'songs/watchlater.html')

    
    
    
    
def channel(request,channel):
    chan=Channel.objects.filter(name=channel).first()
    m_ids=str(chan.music).split(" ")[1:]
    print(m_ids)
    
    preserved=Case(*[When(pk=pk,then=pos) for pos,pk  in enumerate(m_ids)])
    song=Music.objects.filter(id__in=m_ids).order_by(preserved) 
    return render(request,"songs/channel.html",{'channel':chan,"song":song})

def upload(request):
    if request.method=="POST":
        music_name=request.POST.get('name')
        music_singer=request.POST.get('Singername')
        music_movie=request.POST.get('Moviename')
        music_durations=request.POST.get('duration')
        image=request.FILES['image']
        category=request.POST.get('category')
        audio=request.FILES['audio']
        pub_date=request.POST.get('pub_date')
        
        music=Music(music_name=music_name,music_singer=music_singer,music_movie=music_movie,music_durations=music_durations,image=image,audio=audio,pub_date=pub_date)
        
        music.save()
        
        music_id=music.id
        channel_find=Channel.objects.filter(name=str(request.user))
        print(channel_find)
        for i in channel_find:
            i.music+=f" {music_id}"
            i.save()
    
    return  render(request,"songs/upload.html")

def search(request):
    query=request.GET.get("query")
    song=Music.objects.all()
    qs=song.filter(music_name__icontains=query)
    
    return render(request,'songs/search.html',{'song':qs,'search':query})
    