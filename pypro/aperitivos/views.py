from django.shortcuts import render


def video(requests, slug):
    videos = {
        'motivacao': dict(titulo='Video Aperitivo: Motivação', vimeo_id=337049273),
        'instalacao-windows': dict(titulo='Video Aperitivo: Instalação Windows', vimeo_id=337049273),
    }
    video = videos[slug]
    return render(requests, 'aperitivos/video.html', context=dict(video=video))
