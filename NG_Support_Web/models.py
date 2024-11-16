from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    keywords = models.TextField()

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=200, default="Untitled Listing")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="listings", default=1
    )
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20)
    thumbnail = models.ImageField(
        upload_to="thumbnails/", blank=True, null=True, default="static/img/l-4.jpg"
    )
    images = models.ManyToManyField("Image", related_name="listings")
    country = models.CharField(max_length=100, default="Unknown")
    city = models.CharField(max_length=100, default="Unknown")
    location = models.CharField(max_length=255, default="")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    video_link = models.URLField(blank=True)
    amenities = models.ManyToManyField("Amenity", related_name="listings", blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return f"Image {self.id}"

class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class HouseRent(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="house_rents",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200, default="House Rental")
    description = models.TextField(blank=True)
    contact_number = models.CharField(max_length=30)
    address = models.CharField(max_length=255, default="")
    location = models.CharField(max_length=255, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField(default=1)
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True,
        default="static/img/landing-bg.png",
    )
    images = models.ManyToManyField("Image", related_name="house_rents", blank=True)
    country = models.CharField(max_length=100, default="Unknown")
    city = models.CharField(max_length=100, default="Unknown")
    amenities = models.ManyToManyField(
        "Amenity", related_name="house_rents", blank=True
    )

    def __str__(self):
        return self.title


class Job(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="jobs", blank=True, null=True
    )
    title = models.CharField(max_length=200)
    description = RichTextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, default="N/A")
    address = models.CharField(max_length=255, default="")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact_email = models.EmailField()
    posted_on = models.DateTimeField(auto_now_add=True)
    required_skills = models.ManyToManyField("Skill", related_name="jobs", blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    keywords = models.TextField(default="N/A")
    thumbnail = models.ImageField(
        upload_to="service_thumbnails/", null=True, blank=True
    )
    country = models.CharField(max_length=100, default="Unknown")
    city = models.CharField(max_length=100, default="Unknown")
    location = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=15, default="N/A")
    service_amenities = models.ManyToManyField(
        "Service_Amenity", related_name="services_list", blank=True
    )

    def __str__(self):
        return self.title


class Service_Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
