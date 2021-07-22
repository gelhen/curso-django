from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='337049273'),
    Video(slug='instalacao-windows', titulo='Video Aperitivo: Instalação Windows', vimeo_id='337049273'),
]

videos_dct = {v.slug: v for v in videos}

def indice(requests):
    return render(requests, 'aperitivos/indice.html', context={'videos': videos})

def video(requests, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(requests, 'aperitivos/video.html', context=dict(video=video))
