from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from .forms import AlbumForm, ServicesForm, QualForm
from BastianWorld.models import Album, AlbumImage, Services, Qualifications, Contakt, Start

def start(request):
    starts = Start.objects.all().order_by()
    return render(request, 'start.html', {'starts': starts})

def services(request):
    services = Services.objects.all().order_by('-published_date')
    return render(request, 'services.html', {'services': services})


def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) 
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album
     def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context


def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

def qualifications(request):
    quals = Qualifications.objects.all().order_by('-published_date')
    return render(request, 'qualifications.html', {'quals': quals})

def contact(request):
    contacts = Contakt.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})

