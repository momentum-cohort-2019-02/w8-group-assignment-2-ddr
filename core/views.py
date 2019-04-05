from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, User, Card, Quiz
from .forms import DeckForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, JsonResponse
from django.forms.widgets import TextInput
from django.core import serializers
import datetime
import json


def index(request):
    """View function for home page of site."""

    deck_list = Deck.objects.all()
    user = User.objects.all()

    context = {
        'deck_list': deck_list,
        'user': user,
    }
    # Render the HTML template index.html with the date in the context variable
    return render(request, 'index.html', context=context)


def deck_list_view(request):
    deck_list = Deck.objects.all()
    user = User.objects.all()

    context = {
        'deck_list': deck_list,
        'user': user,
    }
    # Render the HTML template index.html with the date in the context variable
    return render(request, 'core/deck_list.html', context=context)


def deck_detail_view(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    paginator = Paginator(deck.cards.all(), 24)

    page = request.GET.get('page')
    cards = paginator.get_page(page)
    context = {
        'cards': cards,
    }
    # Render the HTML template index.html with the date in the context variable
    return render(request, 'core/deck_detail.html', context=context)


# class CreateDeck(CreateView):
#     model = Deck
#     fields = ['name']


@require_http_methods(['POST'])
@login_required
def create_deck_view(request):
    if request.method == "POST":
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('deck_detail', slug=deck.slug)
    else:
        form = DeckForm()
    return render(request, 'core/deck_list.html', {'form': form, })


def card_list_view(request):
    card_list = Card.objects.all()
    paginator = Paginator(card_list, 24)

    page = request.GET.get('page')
    cards = paginator.get_page(page)
    context = {
        'cards': cards,
    }
    # Render the HTML template index.html with the date in the context variable
    return render(request, 'core/card_list.html', context=context)

def quiz_view(request, slug):

    deck = Deck.objects.get(slug=slug)
    cards = deck.cards.all()
    data = {}
    for card in cards:
        data[card.front]={'front':card.front, 'back':card.back}

    if request.is_ajax():
        return JsonResponse(data, content_type='application/json')

    return render(request, 'core/quiz.html', context = {'deck': deck})


@require_http_methods(['POST'])
@login_required
def deck_favorite_view(request, slug):
    deck = get_object_or_404(Deck, slug=slug)

    if deck in request.user.favorited.all():
        request.user.favorited.remove(deck)
        messages.success(request, f"You have favorited {deck.name}.")
    else:
        request.user.favorited.add(deck)
        messages.info(request, f"You have unfavorited {deck.name}.")

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def user_page_view(request):
    # user = get_object_or_404(User)

    return render(request, 'core/user_page.html')
