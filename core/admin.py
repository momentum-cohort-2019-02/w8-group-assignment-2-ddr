from django.contrib import admin
from core.models import Deck, Card
# Register your models here.



@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('name', )}


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('back', )}