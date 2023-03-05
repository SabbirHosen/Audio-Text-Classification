from django.shortcuts import render, HttpResponse, redirect
from .analysis import text_to_emotion, get_large_audio_transcription
from .models import UploadFile


# Create your views here.
def home(request):
    data = {
        'title': 'Emotion Detection'
    }
    return render(request, 'index.html', context=data)


def text_input(request):
    print(request)
    if request.method == "POST":
        input_text = request.POST.get('text')
        results = text_to_emotion(input_text)

        data = {
            'title': 'Result of Emotion Detection',
            'results': results,
            'text': input_text,
            'top': results[0]
        }
        # print(data)
        return render(request, 'index.html', context=data)
        # return redirect('emotionDetection:home')
    return redirect('emotionDetection:home')


def audio_input(request):
    # print(request)
    if request.method == "POST":
        input_text = request.FILES.get('video-file-upload')
        # print(input_text)
        file_obj = UploadFile()
        file_obj.file = input_text
        file_obj.save()
        #
        new_f = UploadFile.objects.last()
        add_url = str(new_f.file.url)
        print(f'E:/NSU Project/project/audioTextClassification/{add_url[1:]}')
        path = f'E:/NSU Project/project/audioTextClassification/{add_url[1:]}'
        # print()
        # sound = AudioSegment.from_mp3(add_url[1:])
        # print('')
        # with open('../media/audio/death.mp3') as o
        text = get_large_audio_transcription(path)
        results = text_to_emotion(text)
        data = {
            'title': 'Result of Emotion Detection',
            'results': results,
            'text': text,
            'top': results[0]
        }
        # print(data)
        new_f.delete()
        return render(request, 'index.html', context=data)
        # return redirect('emotionDetection:home')
    return redirect('emotionDetection:home')


# def processing(request, text):
#     results = text_to_emotion(text)
#     data = {
#         'title': 'Result of Emotion Detection',
#         'results': results,
#         'text': text,
#         'top': results[0]
#     }
#     # print(data)
#     return render(request, 'index.html', context=data)