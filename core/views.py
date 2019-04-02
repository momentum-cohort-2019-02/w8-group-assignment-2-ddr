from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, User, Card, Quiz
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.forms.widgets import TextInput
import datetime


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
    pass

def deck_detail_view():
    pass

def create_deck_view():
    pass

def card_list_view():
    pass

def card_edit_view():
    pass

def create_card_view():
    pass

def quiz_view():
    pass

def user_page_view():
    pass
