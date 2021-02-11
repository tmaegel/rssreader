from django.shortcuts import render, get_object_or_404, redirect

import feedparser

from .forms import FeedForm
from .models import (
    Feed
)


# List the articels of all feeds (rss)
def feed_list_all(request):
    feed_detail_list = []  # List of all feed details (e.g. articles)
    feed_list = Feed.objects.all()  # List of all feeds (rss)
    for feed_entry in feed_list:
        feed_obj = get_object_or_404(Feed, id=feed_entry.id)
        if feed_obj.url:
            feed = feedparser.parse(feed_obj.url)  # Parsing XML data
            feed_detail_list.append(feed)

    context = {
        'feed_list': feed_list,
        'feed_detail_list': feed_detail_list
    }
    return render(request, 'feed/feed_list.html', context)


# List the article of one (by id) feed (rss)
def feed_list_detail(request, feed_id):
    feed_list = Feed.objects.all()  # List of all feeds (rss)
    feed_obj = get_object_or_404(Feed, id=feed_id)
    if feed_obj.url:
        feed_detail = feedparser.parse(feed_obj.url)  # Parsing XML data
    else:
        feed_detail = None

    context = {
        'feed_list': feed_list,
        'feed_detail': feed_detail
    }
    return render(request, 'feed/feed_detail.html', context)


def feed_add_view(request):
    feed_list = Feed.objects.all()  # List of all feeds (rss)
    feed_obj = FeedForm(request.POST or None)  # Only for POST
    if feed_obj.is_valid():
        feed_obj.save()
        return redirect('../')

    context = {
        'feed_list': feed_list,
        'form': feed_obj
    }
    return render(request, 'feed/feed_add.html', context)


def feed_delete_view(request, feed_id):
    feed_list = Feed.objects.all()  # List of all feeds (rss)
    feed_obj = get_object_or_404(Feed, id=feed_id)
    if request.method == 'POST':
        feed_obj.delete()
        return redirect('../../')
    context = {
        'feed_list': feed_list,
        'object': feed_obj,
    }
    return render(request, 'feed/feed_delete.html', context)


def feed_edit_view(request, feed_id):
    feed_list = Feed.objects.all()  # List of all feeds (rss)
    feed_obj = get_object_or_404(Feed, id=feed_id)
    form = FeedForm(request.POST or None, instance=feed_obj)  # Only for POST
    if form.is_valid():
        form.save()
        form = FeedForm()  # Clear the form
        return redirect('../../', object=form)

    context = {
        'feed_list': feed_list,
        'form': form
    }
    return render(request, 'feed/feed_edit.html', context)
