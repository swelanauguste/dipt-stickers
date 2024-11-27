import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class User(AbstractUser):
    # ROLE_CHOICES = (
    #     ("clerk", "Clerk"),
    #     ("technician", "Technician"),
    #     ("manager", "Manager"),
    #     ("user", "User"),
    # )
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    # role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="user")
    job_title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=7, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ["username"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("get-user-detail", kwargs={"slug": self.slug})

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.email}"
