from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Deck(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    favorited_by = models.ManyToManyField(User, related_name="favorited", blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        # If the slug is already set, stop here.
        if self.slug:
            return
        
        base_slug = slugify(self.name)
        slug = base_slug
        n = 0

        while Deck.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

    # def get_absolute_url(self):
    #     return reverse('deck_detail', args=[str(self.slug)])


class Quiz(models.Model):
    rounds = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE,)
    

class Card(models.Model):
    decks = models.ManyToManyField(Deck, related_name='cards')
    front = models.CharField(max_length=50)
    front_image_path = models.CharField(blank=True, null=True, max_length=255)
    category = models.CharField(max_length=50)
    back = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.front} | {self.back}"

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        # If the slug is already set, stop here.
        if self.slug:
            return
        
        base_slug = slugify(self.front + self.back)
        slug = base_slug
        n = 0

        while Card.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug