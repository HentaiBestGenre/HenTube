from django.shortcuts import render
from .models import Channels, Subscriptions
from Videos.models import Videos
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def channel(request, channel_id):
    chan = Channels.objects.get(pk=channel_id)
    videos = Videos.objects.filter(publisher_id=channel_id).order_by('-pub_date')
    if channel_id != request.user.id:
        isSubscribed = bool(Subscriptions.objects.filter(
            subscriber_id=request.user.id,
            subscription_id=channel_id,
        ))
    else:
        isSubscribed = False
    return render(request, 'Channels/Index.html', {'channel': chan,
                                                   'videos': videos,
                                                   'isSubscribed': isSubscribed})


@login_required(login_url='Users:login')
def subscribe(request):
    if request.POST['value'] == 'true':
        Subscriptions.objects.filter(
            subscriber_id=int(request.POST['subscriber']),
            subscription_id=int(request.POST['subscription']),
        ).delete()
        Channels.objects.get(pk=int(request.POST['subscription'])).add_subscriber(-1)
        value = 'false'
    else:
        Subscriptions(
            subscriber_id=request.POST['subscriber'],
            subscription_id=request.POST['subscription'],
        ).save()
        Channels.objects.get(pk=int(request.POST['subscription'])).add_subscriber(1)
        value = 'true'
    return JsonResponse({'status': 200, 'value': value}, status=200)
