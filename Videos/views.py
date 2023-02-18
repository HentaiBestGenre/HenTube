from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import UploadVideoForm, AddCommentForm
from .models import Videos, Reactions, Comments
import sqlite3


con = sqlite3.connect('../db.sqlite3', check_same_thread=False)
cur = con.cursor()


def video(request, video_id):
    v = Videos.objects.get(pk=video_id)
    likes = v.get_likes()
    dislikes = v.get_dislikes()
    comments = v.get_comments()[:20]
    return render(request, 'Videos/Index.html', {'video': v, 'likes': likes,
                                                 'dislikes': dislikes, 'comments': comments,
                                                 })


@login_required(login_url='Users:login')
def upload_video(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = request.FILES['video']
            new_preview = request.FILES['preview']
            safe_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            new_video.name = safe_name
            new_preview.name = safe_name + '.' + new_preview.name.split('.')[-1]
            Videos(
                title=form.cleaned_data['title'],
                video_path=new_video,
                preview_path=new_preview,
                publisher=request.user,
            ).save()
    form = UploadVideoForm()
    return render(request, 'Videos/upload_video.html', {'UploadVideoForm': form})


@login_required(login_url='Users:login')
def react(request):
    value = True if request.POST['value'] == 'like' else False
    video = Videos.objects.get(pk=request.POST['video_id'])
    record = Reactions.objects.filter(
        video_id=request.POST['video_id'],
        author_id=request.POST['author_id'],
    ).first()
    if record and record.value is value:
        record.delete()
    elif record and record.value is not value:
        record.value = value
        record.save()
    else:
        new_record = Reactions(
            video_id=request.POST['video_id'],
            author_id=request.POST['author_id'],
            value=value
        )
        new_record.save()
    likes = video.get_likes()
    dislikes = video.get_dislikes()
    return JsonResponse({'likes': likes, 'dislikes': dislikes}, status=200)


@login_required(login_url='Users:login')
def create_comment(request):
    form = AddCommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = Comments(
            author_id=request.POST['author_id'],
            video_id=request.POST['video_id'],
            value=request.POST['value'],
        )
        comment.save()
        return JsonResponse({'status': 200, 'value': comment.value, 'username': comment.author.user.username}, status=200)
    return JsonResponse({'status': 500}, status=500)
