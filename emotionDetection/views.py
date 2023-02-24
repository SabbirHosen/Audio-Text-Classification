from django.shortcuts import render, HttpResponse, redirect
from .analysis import text_to_emotion


# Create your views here.
def home(request):
    data = {
        'title': 'Emotion Detection'
    }
    return render(request, 'index.html', context=data)


def text_input(request):
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