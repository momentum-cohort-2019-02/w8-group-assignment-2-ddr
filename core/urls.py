from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('decks', views.deck_list_view, name='deck_list'),
    path('decks/<slug:slug>', views.deck_detail_view, name='deck_detail'),
    path('decks/<slug:slug>/favorite',
         views.deck_favorite_view, name="deck_favorite"),
    path('decks/create/', views.create_deck_view, name='create_deck'),
    path('decks/<slug:slug>/edit/', views.edit_deck_view, name="deck_edit"),
    path('cards/', views.card_list_view, name='card_list'),
    path('decks/<slug:slug>/quiz', views.quiz_view, name='quiz'),
    # path('users/<user:username>', views.user_page_view, name='user_page'),
    # path('cards/<slug:slug>/edit/', views.card_edit_view, name='card_edit'),
    # path('cards/create/', views.create_card_view, name='create_card'),
    path('profile/', views.user_page_view, name='user_page'),

]
