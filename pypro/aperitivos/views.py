from django.shortcuts import render


def video(requests, slug):
    video = dict(titulo='Video Aperitivo: Motivação', vimeo_id=337049273)
    return render(requests, 'aperitivos/video.html', context=dict(video=video))
