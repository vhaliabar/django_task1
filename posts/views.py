from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import RegisteredUser, FeedItem
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse



def LikeFeedView(request, pk):
    feed = get_object_or_404(FeedItem, id=request.POST.get('feed_id'))
    liked = False
    if feed.liked.filter(id=request.user.id).exists():
        feed.liked.remove(request.user)
        liked=False
    else:
        feed.liked.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('feed_detail', args=[str(pk)]))

# Create your views here.
def home(request):
    return render(request, 'posts/home.html', {'time': datetime.today() })

class FeedList(ListView):
    model = FeedItem
    context_object_name = 'feeds'
    template_name = 'posts/feeditems_list.html'
    #login_url = '/admin'
    
    #def get_queryset(self):
    #    return self.request.user.notes.all()

class UserFeedList(ListView):
    model = FeedItem
    context_object_name = 'feeds'
    template_name = 'posts/user_feeds.html'
    #login_url = '/admin'
    
    def get_queryset(self):
        return FeedItem.objects.filter(user=self.kwargs['user'])

class FeedDetailView(DetailView):
    model = FeedItem
    context_object_name = 'feed'
    template_name = 'posts/feed_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(FeedDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(FeedItem, id=self.kwargs['pk'])
        
        liked = False
        if stuff.liked.filter(id=self.request.user.id).exists():
            liked=True
        
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context