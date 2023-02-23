from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import pipeline


def text_to_emotion(text):
    model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
    tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, top_k=None)
    result = [{'label': r['label'], 'score': round((r['score']*100), 3)} for r in classifier(text)[0]]
    return result
