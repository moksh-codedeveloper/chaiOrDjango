from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from .models import Tweet
from .forms import TweetForms, UserRegisteration
from django.contrib.auth.views import LoginView
# NEW: Custom login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


def tweet_list(request):
    try:
        print("Authenticated user:", request.user)
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'tweet_list.html', {'tweets': tweets})
    except Exception as e:
        return render(request, 'tweet_list.html', {'tweets': [], 'error': 'Unable to load tweets.'})

@login_required(login_url='login')
def tweet_create(request):
    try:
        if request.method == "POST":
            form = TweetForms(request.POST, request.FILES)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('tweet_list')
        else:
            form = TweetForms()
        return render(request, 'tweet_form.html', {"form": form})
    except Exception as e:
        return render(request, 'tweet_form.html', {"form": TweetForms(), "error": str(e)})

@login_required(login_url='login')
def tweet_edit(request, tweet_id):
    try:
        tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
        if request.method == "POST":
            form = TweetForms(request.POST, request.FILES, instance=tweet)
            if form.is_valid():
                form.save()
                return redirect('tweet_list')
        else:
            form = TweetForms(instance=tweet)
        return render(request, 'tweet_form.html', {"form": form})
    except Exception as e:
        return render(request, 'tweet_form.html', {"form": TweetForms(), "error": str(e)})

@login_required(login_url='login')
def tweet_delete(request, tweet_id):
    try:
        tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
        if request.method == "POST":
            tweet.delete()
            return redirect('tweet_list')
        return render(request, "tweet_confirm_delete.html", {"tweet": tweet})
    except Exception as e:
        return render(request, "tweet_confirm_delete.html", {"error": str(e)})
    

def register(request):
    try:
        if request.method == "POST":
            form = UserRegisteration(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                
                # Log the user in immediately
                login(request, user)
                print("User authenticated:", request.user)

                # ✅ Return a redirect response (MUST)
                return redirect('tweet_list')
            else:
                print("Form errors:", form.errors)  # Debug any issue
        else:
            form = UserRegisteration()

        return render(request, 'registration/register.html', {"form": form})

    except Exception as e:
        return render(request, 'registration/register.html', {
            "form": UserRegisteration(), 
            "error": str(e)
        })

@login_required(login_url='login')
def tweet_search(request):
    try:
        query = request.GET.get('q', '')
        if query:
            results = Tweet.objects.filter(
                Q(text__icontains=query) | Q(user__username__icontains=query)
            ).order_by('-created_at')
        else:
            results = Tweet.objects.none()
        return render(request, 'tweet_search.html', {'results': results, 'query': query, "user": request.user})
    except Exception as e:
        return render(request, 'tweet_search.html', {"error": str(e)})
