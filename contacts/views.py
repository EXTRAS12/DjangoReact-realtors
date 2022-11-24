from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response


class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                data['subject'],
                'Имя: '
                + data['name']
                + '\Email: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'blabla@mail.ru',
                ['blabla@mail.ru'],
                fail_silently=False
            )
            contact = Contact(name=data['name'], email=data['email'],
                              subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'Успешно': 'Сообщение отправлено!'})

        except:
            return Response({'Ошибка': 'Сообщение не отправлено!'})
