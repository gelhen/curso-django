from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

def indice(requests):
    videos = Video.objects.order_by('creation').all()
    return render(requests, 'aperitivos/indice.html', context={'videos': videos})

def video(requests, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(requests, 'aperitivos/video.html', context=dict(video=video))
