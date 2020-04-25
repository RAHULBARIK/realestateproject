from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,

    }
    return render(request, 'pages/listings.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
