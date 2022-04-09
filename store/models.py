from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True)
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    def __str__(self):
        return f'{self.id}: {self.name}'


class UserBookRelation(models.Model):
    RATE_CHOICES = [
        (1, 'I hated it'),
        (2, 'I didnt like it'),
        (3, 'it was ok'),
        (4, 'I liked it'),
        (5, 'I loved it'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.book.name}, {self.rate}'

    def save(self, *args, **kwargs):
        from store.logic import set_rating

        creating = not self.pk

        old_rating = self.rate
        super().save(*args, **kwargs)
        new_rating = self.rate

        if old_rating != new_rating or creating:
            set_rating(self.book)
