from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# create database model for chatroom
class ChatRoom(models.Model):
    ENGLISH = 'EN'
    FRENCH = 'FR'
    SPANISH = 'ES'
    CHINESE = 'ZH'
    JAPANESE = 'JA'
    LANGUAGE_CHOICES = [(ENGLISH, 'English'),
                        (FRENCH, 'French'),
                        (SPANISH, 'Spanish'),
                        (CHINESE, 'Chinese'),
                        (JAPANESE, 'Japanese')]
    name = models.CharField(max_length=100)
    # the slug to be used for url
    slug = models.SlugField(unique=True)
    room_id = models.BigAutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name="ID",)
    # creation date left blank, will be filled by room creation logic
    creation_date = models.DateTimeField(blank=True, null=True, verbose_name="Creation Date")
    language = models.CharField(max_length=30, choices=LANGUAGE_CHOICES, default='English')
    is_public = models.BooleanField(default=True)
    # number of members in a chat ranges from 1 to 100
    max_member = models.IntegerField(default=50, validators=[MaxValueValidator(100), MinValueValidator(1)])
    num_member = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
