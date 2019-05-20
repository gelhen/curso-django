from django.shortcuts import render


def video(requests, slug):
    return render(requests, 'aperitivos/video.html')
