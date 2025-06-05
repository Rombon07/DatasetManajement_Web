# dataset/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# from .views import test_404


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("upload/", views.upload_dataset, name="upload_dataset"),
    path("mydata/", views.mydata, name="mydata"),
    path("dataset/<int:pk>/", views.dataset_detail, name="dataset_detail"),
    path("dataset/<int:pk>/edit/", views.edit_dataset, name="edit_dataset"),
    path("dataset/<int:pk>/delete/", views.delete_dataset, name="delete_dataset"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path(
        "dataset/<int:dataset_id>/log_action/",
        views.log_dataset_action,
        name="log_dataset_action",
    ),
    # urls.py
    path(
        "dataset/<int:dataset_id>/log_print/",
        views.log_print_action,
        name="log_print_action",
    ),
    path(
        "dataset/<int:dataset_id>/summary-pdf/",
        views.download_summary,
        name="download_summary",
    ),
    path("dataset/<int:pk>/print/", views.print_dataset, name="print_dataset"),
    path("api/dataset/<int:dataset_id>/", views.api_dataset, name="api_dataset"),
    # path("tes-404/", test_404),  # Tambahkan ini untuk tes halaman 404
]
