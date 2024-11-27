from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from . import forms
from .forms import StickerForm
from .models import Sticker


@login_required
def sticker_view(request):
    # Get all stickers created by the logged-in user
    stickers = Sticker.objects.filter(
        created_by=request.user, created_at__date=now().date()
    )

    if request.method == "POST":
        # Process the sticker creation form
        form = forms.StickerForm(request.POST)
        if form.is_valid():
            sticker = form.save(commit=False)
            sticker.created_by = request.user
            sticker.updated_by = request.user
            sticker.save()
            return redirect("stickers")
    else:
        # Initialize an empty form for GET requests
        form = forms.StickerForm()

    # Render the template with the form and sticker list
    context = {"form": form, "stickers": stickers}
    return render(request, "stickers/stickers.html", context)


class StickerListView(LoginRequiredMixin, ListView):
    model = Sticker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stickers"] = Sticker.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get("stickers")

        if query:
            return Sticker.objects.filter(
                Q(name__icontains=query)
                | Q(no_plate__icontains=query)
                | Q(sticker__icontains=query)
            ).distinct()
        return Sticker.objects.all()


class StickerDetailView(LoginRequiredMixin, DetailView):
    model = Sticker


class StickerCreateView(LoginRequiredMixin, CreateView):
    model = Sticker
    form_class = StickerForm
    success_url = reverse_lazy("stickers")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class StickerUpdateView(LoginRequiredMixin, UpdateView):
    model = Sticker
    form_class = StickerForm
    success_url = reverse_lazy("stickers")

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
