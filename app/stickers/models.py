from dateutil.relativedelta import relativedelta
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify
from users.models import User


def expiration_date():
    return timezone.now() + relativedelta(years=1)


class Sticker(models.Model):
    name = models.CharField(max_length=100, blank=True)
    sticker = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    no_plate = models.CharField("number plate", max_length=100, blank=True)
    expires = models.DateField(
        null=True, default=expiration_date(), help_text="MM/DD/YYYY"
    )
    model = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="sticker_created_by",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="sticker_updated_by",
    )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("sticker", "no_plate")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sticker)
        super(Sticker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("sticker-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.sticker}/{self.expires}/{self.name}/{self.no_plate}"
