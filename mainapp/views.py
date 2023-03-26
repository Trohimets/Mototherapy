import os
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')

@api_view(['POST'])
def feedback_list(request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            send_mail(
                        'Форма обратной связи с сайта "Мототерапия"',
                        (f"Пользователь {serializer.data['name']} отправил вам сообщение: {serializer.data['message']}. " +
                        f"Его телефон: {serializer.data['phone']}, адрес электронной почты: {serializer.data['email']}"),
                        EMAIL_HOST_USER,
                        [RECIPIENT_ADDRESS,],
                        fail_silently=False,
                        ) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)