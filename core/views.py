from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, User, Card, Quiz
from .forms import DeckForm
from django.views import generic
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
        'deck': deck,
        'cards': cards,
    }
    # Render the HTML template index.html with the date in the context variable
    return render(request, 'core/deck_detail.html', context=context)


@login_required
def edit_deck_view(request, slug):
    card_list = Card.objects.all()
    card_paginator = Paginator(card_list, 24)
    page = request.GET.get('cards_page')
    # try:
    #     card_list = card_paginator.page(page)
    # except:
    #     card_list = card_paginator.page(1)

    deck = get_object_or_404(Deck, slug=slug)
    all_deck_cards = deck.cards.all()
    deck_paginator = Paginator(deck.cards.all(), 24)
    page1 = request.GET.get('deck_page')

    deck_cards = deck_paginator.get_page(page1)
    all_cards = card_paginator.get_page(page)
    context = {
        'deck_cards': deck_cards,
        'all_deck_cards': all_deck_cards,
        'all_cards': all_cards,
        'deck': deck,
    }
    # card_list = Card.objects.all()
    return render(request, 'core/deck_edit.html', context=context)


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


# @require_http_methods(['POST'])


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
    print(cards)
    data = {}
    i = 0
    for card in cards:
        data[i] = {
            'front': card.front,
            'back': card.back,
            'front_image_path': card.front_image_path,
            'card_category': card.category
        }
        i += 1

    if request.is_ajax():
        return JsonResponse(data, content_type='application/json')

    return render(request, 'core/quiz.html', context={'deck': deck})


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


@require_http_methods(['POST'])
@login_required
def add_or_remove_card(request, slug, card_slug):
    deck = get_object_or_404(Deck, slug=slug)
    card = get_object_or_404(Card, slug=card_slug)

    if card in deck.cards.all():
        deck.cards.remove(card)
        messages.info(
            request, f"You have removed {card.front} from {deck.name}")
    else:
        deck.cards.add(card)
        messages.info(request, f"You have added {card.front} to {deck.name}")

    deck = get_object_or_404(Deck, slug=slug)
    deck_cards = deck.cards.all()
    cards = Card.objects.all()
    data = {'card-slug': card.slug}
    # data = {'all_cards': {}, 'deck_cards': {}}
    # data['all_cards'] = {}
    # data['deck_cards'] = {}
    # i = 0
    # x = 0
    # for card in cards:
    #     data['all_cards'][i] = {
    #         'front': card.front,
    #         'back': card.back,
    #         'front_image_path': card.front_image_path,
    #         'card_category': card.category,
    #     }
    #     i += 1

    # for card in deck_cards:
    #     data['deck_cards'][x] = {
    #         'front': card.front,
    #         'back': card.back,
    #         'front_image_path': card.front_image_path,
    #         'card_category': card.category,
    #     }
    #     x += 1

    if request.is_ajax():
        return JsonResponse(data, content_type='application/json', safe=True)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def user_page_view(request):

    return render(request, 'core/user_page.html')
