from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 337049273),
    Video('instalacao-windows', 'Video Aperitivo: Instalação Windows', 337049273),
]

videos_dct = {v.slug: v for v in videos}

def indice(requests):
    return render(requests, 'aperitivos/indice.html', context={'videos': videos})

def video(requests, slug):
    video = videos_dct[slug]
    return render(requests, 'aperitivos/video.html', context=dict(video=video))
