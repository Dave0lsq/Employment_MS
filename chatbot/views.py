import openai
from django import forms
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import EssayQuestion
import random

openai_api_key = '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'
openai.api_key = openai_api_key


def ask_openai(random_question,user_essay):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are an assistant trained to grade essays."},
            {"role": "user", "content": f"Essay Question: {random_question}"},
            {"role": "user", "content": f"Essay Answer: {user_essay}"},
            {"role": "system",
             "content": "Score the Answer based on Question. Score in three areas: Content, Language and Organization, each out of 7 points."}
        ]
    )
    max_tokens = 300
    # print(response)
    answer = response.choices[0].message.content.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        user_essay = request.POST.get('message')
        # Retrieve the question using the ID stored in the session
        question_id = request.session.get('question_id')
        random_question = EssayQuestion.objects.get(id=question_id)

        response = ask_openai(random_question.question_text, user_essay)

        return JsonResponse({'message': user_essay, 'response': response})

    all_questions = list(EssayQuestion.objects.all())
    random_question = random.choice(all_questions)
    # Store the ID of the random question in the session
    request.session['question_id'] = random_question.id

    year_display = dict(EssayQuestion.year_choices)[random_question.year]  # Get the display text for the year

    return render(request, 'chatbot.html', locals())


class EssayQuestionForm(forms.ModelForm):
    class Meta:
        model = EssayQuestion
        fields = ['question_text', 'year']


def add_question(request):
    if request.method == 'POST':
        form = EssayQuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to your chatbot page or wherever you like

    else:
        form = EssayQuestionForm()

    return render(request, 'add_question.html', {'form': form})
