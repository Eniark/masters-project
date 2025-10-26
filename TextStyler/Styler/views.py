from django.shortcuts import render
from transformers import BartTokenizer, BartForConditionalGeneration
import os
from .forms import TranslationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    form = TranslationForm()
    return render(request, "Styler/index.html", {'form': form})


@csrf_exempt
def run_translate(request):
    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            dialect = form.cleaned_data['dialect']
            text = translate(query, dialect)[0]

            
            html = f'''
            <div class="chat-message">
                <div class="user-message">{query}</div>
                <div class="bot-message">{text}</div>
            </div>
            '''
            return HttpResponse(html)
        else:
            return HttpResponse(
                '<div class="chat-message"><div class="bot-message">Неправильний ввід.</div></div>',
                status=400
            )
    return HttpResponse(
        '<div class="chat-message"><div class="bot-message">Неправильний запит.</div></div>',
        status=400
    )


def translate(query, dialect):
    path = os.path.join('Styler', 'BARTmodels', dialect)

    model = BartForConditionalGeneration.from_pretrained(path)
    tokenizer = BartTokenizer.from_pretrained(path)

    tokens = tokenizer(query, truncation=True, padding=True, return_tensors="pt")["input_ids"]

    gen_tokens = model.generate(tokens, max_length=512)
    text = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)

    return text
