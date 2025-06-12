from django.shortcuts import render
from .models import Tweet 
from .forms import TweetForms, UserRegisteration
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "index.html")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForms(request.POST, request.FILES)
        if form.is_valid:
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else :
        form = TweetForms()
    return  render(request, 'tweet_form.html', {"form": form})

@login_required
def tweet_edit (request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        form = TweetForms(request.POST, request.FILES)
        if form.is_valid:
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else :
        form = TweetForms(instance=tweet)
        
    return render(request, 'tweet_form.html', {"form": form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, "tweet_confirm_delete.html", {"tweet": tweet})

def register(request):
    if request.method == "POST":
        form = UserRegisteration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.username = form.cleaned_data['username']
            # user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegisteration()
    return render(request, 'registration/register.html', {"form": form})

def tweet_search(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        if query:
            results = Tweet.objects.filter(
                Q(text__icontains=query) | Q(user__username__icontains=query)
            ).order_by('-created_at')
        else:
            results = Tweet.objects.none()
    return render(request, 'tweet_search.html', {'results': results,'query': query, "user": request.user})