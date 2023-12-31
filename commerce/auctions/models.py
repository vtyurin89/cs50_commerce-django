from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Name')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URL part (unique)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Listing(models.Model):
    creator = models.ForeignKey('User', blank=True, null=True, on_delete=models.PROTECT, related_name="creator",
                                verbose_name='Creator')
    title = models.CharField(max_length=250, db_index=True, verbose_name='Title')
    slug = models.SlugField(max_length=300, db_index=True, unique=True, verbose_name='URL part (slug)')
    cat = models.ForeignKey('Category', null=True, blank=True, verbose_name='Category', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Price')
    description = models.TextField(blank=True, verbose_name='Description')
    image = models.URLField(null=True, blank=True, verbose_name='Image url')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')
    is_active = models.BooleanField(default=True, verbose_name='Is currently active')
    winner = models.ForeignKey('User', blank=True, null=True, on_delete=models.PROTECT,
                               related_name="winner", verbose_name='Winner')
    watchlist = models.ManyToManyField('User', blank=True, null=True, related_name='added_to_watchlist')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_listing', kwargs={'listing_slug': self.slug})

    def usd_price(self):
        return "USD {:,.2f}".format(self.price)


class Bid(models.Model):
    bidder = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Bidder')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, verbose_name='Listing')
    bid_amount = models.FloatField(verbose_name='Bid amount')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f'{self.bidder} bid {self.bid_amount}'

    def usd_bid_amount(self):
        return "USD {:,.2f}".format(self.bid_amount)


class Comment(models.Model):
    comment_text = models.TextField(verbose_name='Comment text')
    comment_author = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Comment author')
    listing = models.ForeignKey('Listing', on_delete=models.PROTECT, verbose_name='Listing')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')
    is_active = models.BooleanField(default=True, verbose_name='Is currently active')

    def __str__(self):
        return f"Comment by {self.comment_author} in '{self.listing}'"


