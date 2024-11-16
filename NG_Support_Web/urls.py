from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_categories/", views.all_categories, name="all_categories"),
    path("add_listing/", views.add_listing, name="add_listing"),
    path("api/amenities/", views.amenities_list, name="amenities_list"),
    path("grid_full_width/", views.grid_full_width, name="grid_full_width"),
    path("add_amenity/", views.add_amenity, name="add_amenity"),
    path("listing_detail/<int:id>", views.listing_detail, name="listing_detail"),
    path("contact/", views.contact, name="contact"),
    path("important_contacts/", views.important_contacts, name="important_contacts"),
    path("Who_is_who/", views.Who_is_who, name="Who_is_who"),
    path("house_rents/", views.house_rent_list, name="house_rent_list"),
    path("house_rents/<int:id>/", views.house_rent_detail, name="house_rent_detail"),
    path("job/", views.job_list, name="job_list"),
    path("jobs/<int:id>/", views.job_detail, name="job_detail"),
    path("apply/", views.apply_view, name="apply"),
    path("services/", views.services, name="services"),
    path("services_list/<str:title>", views.services_list, name="services_list"),
    path("service_detail/<int:id>", views.service_detail, name="service_detail"),
    path("blog/", views.blog, name="blog"),
    path("about_us/", views.about_us, name="about_us"),
    path("business_ad/", views.business_ad, name="business_ad"),
]
