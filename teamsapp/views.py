from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View

from .models import Commands, Pilots, Cars
from .forms import ReviewFrorm


class IndexCommand(ListView):
    """ Список команд """
    model = Commands
    queryset = Commands.objects.all()
    template_name = 'teamsapp/command_list.html'

    # Способ по добавлению сторонней информации из модели.
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pilots'] = Pilots.objects.all()
        return context


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
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.command = command
            form.save()
        return redirect(command.get_absolute_url())


