from django.http import Http404
from django.shortcuts import render, get_object_or_404

from SweetOffer.models import Offer, Type


def index(request):
    types = Type.objects.all()
    context = {'types': types}
    return render(request, 'SweetOffer/index.html', context)


def offer_list(request, type_id):
    offers_by_type = Offer.objects.filter(type_offer=type_id)
    context = {'offers_by_type': offers_by_type}
    return render(request, 'SweetOffer/offer_list.html', context)


def detail(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    return render(request, 'SweetOffer/detail.html', {'offer': offer})
