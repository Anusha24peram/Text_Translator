from django.shortcuts import render  # <-- this is required!
from deep_translator import GoogleTranslator
from textblob import TextBlob

def detect_view(request):
    translated_text = ''
    sentiment_label = ''
    polarity = 0

    if request.method == 'POST':
        input_text = request.POST.get('input_text')

        translated_text = GoogleTranslator(source='auto', target='en').translate(input_text)

        blob = TextBlob(translated_text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment_label = "Positive"
        elif polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

    return render(request, 'translator/detect.html', {
        'translated_text': translated_text,
        'sentiment': sentiment_label,
        'polarity': polarity
    })
