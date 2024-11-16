from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, HouseRent, Image, Job, Listing, Amenity, Service
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import json
from django.contrib import messages


def index(request):
    categories = Category.objects.all()
    results = []

    if request.method == "POST":
        # Check if adding a new category
        if "name" in request.POST:
            name = request.POST.get("name").strip()
            icon = request.POST.get("icon").strip()
            keywords = request.POST.get("keywords").strip()

            # Create a new category
            Category.objects.create(name=name, icon=icon, keywords=keywords)
            return redirect(
                "index"
            )  # Redirect to the same page to see updated categories

        # Searching logic
        keyword = request.POST.get("keywords", "").strip()
        selected_category = request.POST.get("category", "").strip()

        # Start with all categories
        results = Category.objects.all()

        # Apply filters based on keyword and selected category
        if keyword:
            results = results.filter(keywords__icontains=keyword)

        if selected_category:
            results = results.filter(name=selected_category)

    context = {
        "categories": categories,
        "results": results,
    }
    return render(request, "index.html", context)


def all_categories(request):
    # Get all categories from the database
    categories = Category.objects.all()

    # Set up pagination
    paginator = Paginator(categories, 15)  # Show 15 categories per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "all_categories.html", {"page_obj": page_obj})


def add_listing(request):
    categories = Category.objects.all()
    print("____________________", request.method)
    if request.method == "POST":
        title = request.POST.get("title")
        category_id = request.POST.get("category")
        tagline = request.POST.get("tagline")
        description = request.POST.get("description")
        thumbnail = request.FILES.get("thumbnail")
        images = request.FILES.getlist("images")
        contact_number = request.POST.get("contact_number")
        country = request.POST.get("country")
        city = request.POST.get("city")
        location = request.POST.get("location")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        facebook_url = request.POST.get("facebook_url")
        instagram_url = request.POST.get("instagram_url")
        whatsapp_number = request.POST.get("whatsapp_number")
        video_link = request.POST.get("video_link")

        # Handle thumbnail upload
        thumbnail = request.FILES.get("thumbnail")

        # Handle gallery upload
        images = request.FILES.getlist("images")

        # Save thumbnail and gallery images

        if thumbnail:
            fs = FileSystemStorage()
            thumbnail_name = fs.save(thumbnail.name, thumbnail)
        else:
            thumbnail_name = None
        # Create a new listing object

        listing = Listing.objects.create(
            title=title,
            category_id=category_id,
            tagline=tagline,
            description=description,
            contact_number=contact_number,
            thumbnail=thumbnail_name,
            country=country,
            city=city,
            location=location,
            latitude=latitude,
            longitude=longitude,
            facebook_url=facebook_url,
            instagram_url=instagram_url,
            whatsapp_number=whatsapp_number,
            video_link=video_link,
        )

        # Handle gallery upload
        images = request.FILES.getlist("images")

        # Save gallery images
        for image in images:
            image_instance = Image(image=image)
            image_instance.save()
            listing.images.add(image_instance)

        # Save selected amenities
        amenity_ids = request.POST.getlist(
            "amenities"
        )  # Get selected amenity IDs from the form
        listing.amenities.set(amenity_ids)  # Associate amenities with the listing

        # Redirect to the grid_full_width page
        return redirect("grid_full_width")

    return render(request, "add_listing.html", {"categories": categories})


def add_amenity(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amenity_name = data.get("name")
            if amenity_name:
                amenity = Amenity.objects.create(name=amenity_name)
                return JsonResponse({"id": amenity.id, "name": amenity.name})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


def amenities_list(request):
    amenities = Amenity.objects.all().values("id", "name")
    return JsonResponse(list(amenities), safe=False)


def grid_full_width(request):
    listings = Listing.objects.all()  # Fetch all listings
    return render(request, "grid_full_width.html", {"listings": listings})


def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    amenities = listing.amenities.all()
    return render(
        request, "listing_detail.html", {"listing": listing, "amenities": amenities}
    )


def contact(request):
    return render(request, "contact.html")


def important_contacts(request):
    return render(request, "important_contacts.html")


def Who_is_who(request):
    return render(request, "Who_is_who.html")


def house_rent_list(request):
    house_rents = HouseRent.objects.all()
    return render(request, "house_rent_list.html", {"house_rents": house_rents})


def house_rent_detail(request, id):
    house_rent = get_object_or_404(HouseRent, id=id)
    amenities = house_rent.amenities.all()
    return render(
        request,
        "house_rent_detail.html",
        {"house_rent": house_rent, "amenities": amenities},
    )


def job_list(request):
    jobs = Job.objects.all()
    return render(request, "job_list.html", {"jobs": jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    required_skills = job.required_skills.all()
    return render(
        request,
        "job_detail.html",
        {"job_list": job, "required_skills": required_skills},
    )


def apply_view(request):
    if request.method == "POST":
        messages.success(request, "Application submitted successfully!")
        return render(request, "apply.html")

    return render(request, "apply.html")


def services(request):
    # Get all services from the database
    services = Service.objects.all()

    # Set up pagination
    paginator = Paginator(services, 15)  # Show 15 services per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "services.html", {"page_obj": page_obj})


# View to show all services in a grid
def services_list(request, title):
    # Filter services by name/category
    services = Service.objects.filter(title=title)
    return render(request, "services_list.html", {"services": services, "title":title})


# View to show the detail of a specific service
def service_detail(request, id):
    # Fetch a service using the ID
    service = get_object_or_404(Service, id=id)
    amenities = service.service_amenities.all()

    return render(
        request, "service_detail.html", {"service": service, "amenities": amenities}
    )


def blog(request):
    return render(request, "blog.html")


def about_us(request):
    return render(request, "about_us.html")


def business_ad(request):
    return render(request, "business_ad.html")


