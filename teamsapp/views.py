from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View

from .models import Commands, Pilots, Cars
from .forms import ReviewFrorm


# class IndexCommand(View):
#     """ Список команд """
#     def get(self, request):
#         teamsapp = Commands.objects.all()
#         pilots = Pilots.objects.all()
#         return render(request, 'teamsapp/command_list.html', {'command_list': teamsapp, 'pilots': pilots})

class IndexCommand(ListView):
    """ Список команд """

    model = Commands
    queryset = Commands.objects.all()
    template_name = 'teamsapp/command_list.html'


# class Command(View):
#     """ Описание команды"""
#     def get(self, request, slug):
#         command = Commands.objects.get(url=slug)
#         car = Cars.objects.get(command=command.id)
#         return render(request, 'teamsapp/commands_detail.html', {"command": command, "car": car})

class Command(DetailView):
    """ Описание команды"""

    model = Commands
    abracadabra = Commands.objects.all()
    slug_field = 'url'


class AddReview(View):
    """ Отзывы """
    def post(self, request, pk):
        form = ReviewFrorm(request.POST)
        command = Commands.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.command = command
            form.save()
        return redirect(command.get_absolute_url())


