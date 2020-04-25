from django.shortcuts import render, get_object_or_404

from .models import Listing

from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices

    }
    return render(request, 'listings/index.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
