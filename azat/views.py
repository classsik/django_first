from django.shortcuts import render


def home(request):
    fio = 'Юлдашев Азат Ринатович'
    age = 15
    hobbys = 'Программирование, дизайн'
    return render(request, 'azat/index.html', {'fio': fio, 'age': age, 'hobbys': hobbys})


def about(request):
    return render(request, 'azat/about.html', {})


def contacts(request):
    return render(request, 'azat/contacts.html', {})