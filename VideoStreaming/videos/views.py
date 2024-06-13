from django.shortcuts import render, get_object_or_404
from .models import Video, Comment
from django.db.models import Q


# def video_list(request):

def video_list(request):
    videos = Video.objects.all()
    query = request.GET.get('q')
    if query:
        videos = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})



def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(video=video, content=content)
    comments = video.comments.all()
    return render(request, 'videos/video_detail.html', {'video': video, 'comments': comments})

