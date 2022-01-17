from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm
from django.core.mail import EmailMessage


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #if form.is_valid():
            #form.save()
        email = EmailMessage(
            'Hello',
            'Body goes here',
            'from@example.com',
            ['andrey.pwn@gmail.com'],
            ['andrey.pwn@gmail.com'],
            reply_to=['andrey.pwn@gmail.com'],
            headers={'Message-ID': 'foo'},
        )
        email.send()
        return render(request, 'main/index.html')

    form = ContactForm()
    context = {'form': form}
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     send_mail(
    #         'Subject here',
    #         'Here is the message.',
    #         'andrey.pwn@gmail.com',
    #         ['andrey.pwn@gmail.com'],
    #         fail_silently=False,
    #     )
    #     # create a form instance and populate it with data from the request:
    #     form = ContactForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as requestuired
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/thanks/')
    #
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = ContactForm()

    return render(request, 'main/index.html', context)
