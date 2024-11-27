from django.urls import path

from . import views

urlpatterns = [
    # path("sticker-list/", views.StickerListView.as_view(), name="sticker-list"),
    path("", views.sticker_view, name="stickers"),
    path("stickers/create/", views.StickerCreateView.as_view(), name="sticker-create"),
    path(
        "stickers/<slug:slug>/", views.StickerDetailView.as_view(), name="sticker-detail"
    ),
    path(
        "stickers/<slug:slug>/update/",
        views.StickerUpdateView.as_view(),
        name="sticker-update",
    ),
]
