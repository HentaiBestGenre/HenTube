from django.shortcuts import render
from Videos.models import Videos


def main_page(request):
    videos = Videos.objects.order_by('-pub_date')[:10]
    return render(request, 'main_page/main_page.html', {"videos": videos})

