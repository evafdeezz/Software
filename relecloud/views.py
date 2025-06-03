from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg  # Para calcular la media de valoraciones
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models
from .models import Review


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


from django.db.models import Count, Avg

from django.db.models import Count

def destinations(request):
    show_all = request.GET.get('show_all') == '1'  # Verifica si se deben mostrar todos los destinos

    # Anotar popularidad basada en el número de reseñas, pero con un nombre único
    annotated_destinations = models.Destination.objects.annotate(
        calculated_popularity=Count('reviews')
    ).order_by('-calculated_popularity')  # Ordenar por popularidad calculada

    if not show_all:
        annotated_destinations = annotated_destinations[:3]  # Limitar a los 3 más populares

    return render(request, 'destinations.html', {
        'destinations': annotated_destinations,
        'show_all': show_all
    })




class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'


class DestinationCreateView(generic.CreateView):
    model = models.Destination
    template_name = 'destination_form.html'
    fields = ['name', 'description','image']


class DestinationUpdateView(generic.UpdateView):
    model = models.Destination
    template_name = 'destination_form.html'
    fields = ['name', 'description','image']


class DestinationDeleteView(generic.DeleteView):
    model = models.Destination
    template_name = 'destination_confirm_delete.html'
    success_url = reverse_lazy('destinations')


class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'


class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Enviar correo al cliente
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        cruise = form.cleaned_data['cruise']

        subject = "Thank you for your information request"
        message = f"Hi {name},\n\nThank you for your interest in our cruise: {cruise}. We will get back to you soon with more details. You can continue navegating.\n\nBest regards,\nReleCloud Team"
        from_email = 'raulete2000@yahoo.es'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return response


def cruise_detail(request, cruise_id):
    cruise = get_object_or_404(models.Cruise, id=cruise_id)
    reviews = cruise.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.cruise = cruise
            review.save()
    else:
        form = ReviewForm()

    return render(request, 'cruise_detail.html', {
        'cruise': cruise,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    })


def destination_detail(request, destination_id):
    destination = get_object_or_404(models.Destination, id=destination_id)
    reviews = destination.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.destination = destination
            review.save()
    else:
        form = ReviewForm()

    return render(request, 'destination_detail.html', {
        'destination': destination,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    })


# Formularios
class InfoRequestForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    def __init__(self, *args, **kwargs):
        super(InfoRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
