from django.urls import path
from . import views

urlpatterns = [
    path("operations/", views.student),
    path("update/<int:id>", views.update_student),
    path("view-all/", views.view_all_student),
    path("delete/<int:id>/", views.delete_by_id),
]