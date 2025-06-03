from django.db import models
from django.urls import reverse #Comentario

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    popularity = models.IntegerField(
        default=0,  # Popularidad predeterminada en 0
        null=False
    )
    image = models.ImageField(
        upload_to='destinations/',  # Carpeta donde se guardarán las imágenes
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={"pk": self.pk})
    
def destination_detail(request, destination_id):
    destination = get_object_or_404(models.Destination, id=destination_id)
    reviews = destination.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    popularity = reviews.count()  # Número de reseñas como popularidad

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
        'popularity': popularity,
        'form': form,
    })

    

class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    destinations = models.ManyToManyField(
        Destination,
        related_name='cruises'
    )
    def __str__(self):
        return self.name

class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.PROTECT
    )

class Review(models.Model):
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    cruise = models.ForeignKey('Cruise', on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rango de 1 a 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating} - {self.comment[:30]}"