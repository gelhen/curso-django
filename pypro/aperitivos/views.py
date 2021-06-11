from django.shortcuts import render

videos = [
    dict(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id=337049273),
    dict(slug='instalacao-windows', titulo='Video Aperitivo: Instalação Windows', vimeo_id=337049273),
]

videos_dct = {dct['slug']: dct for dct in videos}

def indice(requests):
    return render(requests, 'aperitivos/indice.html', context={'videos': videos})

def video(requests, slug):
    video = videos_dct[slug]
    return render(requests, 'aperitivos/video.html', context=dict(video=video))
