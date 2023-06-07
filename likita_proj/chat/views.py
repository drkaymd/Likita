from django.shortcuts import render
from django.http import JsonResponse
import openai
import os
from django.utils import timezone
from .models import Chat
from datetime import datetime
import pytz # import pytz for timezone localization

openai.api_key = os.environ.get('CHATBOT_API_KEY')

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )    
    answer = response.choices[0].message.content.strip()
    return answer


current_time = datetime.now().strftime("%HH:%MM:%SS")

def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_openai(message)

        # chat = Chat(user=request.user, message=message,
        #             response=response, created_at=current_time)
        # chat.save()

        return JsonResponse({'response': response, 'message': message})
    context = {'chats': chats}
    return render(request, 'chat/chat.html', context)

