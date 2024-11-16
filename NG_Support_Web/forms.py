from django import forms
from .models import Amenity, Category, HouseRent, Job, Listing, Service


class CategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = ["name", "icon", "keywords"]


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "thumbnail",
            "images",
            "contact_number",
            "country",
            "city",
            "location",
            "category",
            "latitude",
            "longitude",
            "tagline",
            "description",
            "facebook_url",
            "instagram_url",
            "whatsapp_number",
            "video_link",
        ]

    def clean_images(self):
        images = self.cleaned_data.get("images")
        return images


class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ["name"]


class HouseRentForm(forms.ModelForm):
    class Meta:
        model = HouseRent
        fields = [
            "category",
            "title",
            "thumbnail",
            "images",
            "contact_number",
            "address",
            "location",
            "price",
            "bedrooms",
            "description",
            "country",
            "city",
        ]

    def clean_images(self):
        images = self.cleaned_data.get("images")
        return images


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "category",
            "title",
            "company",
            "location",
            "salary",
            "description",
            "contact_email",
            "required_skills",
            "contact_number",
            "address",
        ]

    def clean_required_skills(self):
        skills = self.cleaned_data.get("required_skills")
        return skills


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "name",
            "description",
            "icon",
            "keywords",
            "location",
            "contact_number",
            "amenities",
            "thumbnail",
            "title",
            "city",
            "country",
        ]
