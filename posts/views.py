from django.shortcuts import render
from datetime import datetime
from .models import RegisteredUser, FeedItem
from django.views.generic import CreateView, UpdateView, ListView, DetailView



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