from django.http import Http404
from django.shortcuts import render, get_object_or_404

from SweetOffer.models import Offer


def index(request):
    latest_offers_list = Offer.objects.order_by('-pub_date')[:5]
    context = {'latest_offers_list': latest_offers_list}
    return render(request, 'SweetOffer/index.html', context)


def detail(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    return render(request, 'SweetOffer/detail.html', {'offer': offer})

