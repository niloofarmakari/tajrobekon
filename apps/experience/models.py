from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager


# class TypeChoices(models.TextChoices):
#     WORK = "work", _("Work")
#     EDUCATION = "education", _("Education")
#     MIGRATION = "migration", _("Migration")
#     SHOPPING = "SHOPPING", _("Shopping")
#     PERSONAL = "PERSONAL", _("Personal")
#     TECHNICAL = "TECHNICAL", _("Technical")
#     INDUSTRIAL = "INDUSTRIAL", _("Industrial")
#     SOCIAL = "SOCIAL", _("Social")
#     ENTERTAINMENT = "ENTERTAINMENT", _("Entertainment")
#     ACCIDENT = "ACCIDENT", _("Accident")
#     QUOTE = "QUOTE", _("Quote")
#     OTHER = "other", _("Other")


class ExperienceCategory(models.Model):
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))
    slug = models.SlugField(max_length=100, primary_key=True)
    description = models.TextField(
        default="",
        blank=True,
        verbose_name=_("Category Description"),
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Experience publish time"))

    def __str__(self):
        return self.name


class Experience(models.Model):
    class TypeChoices(models.TextChoices):
        FREE = "free", _("Free")
        QUOTE = "quote", _("Quote")

    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.FREE,
        verbose_name=_("Experience Type"),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(ExperienceCategory, verbose_name=_("Experience Category"), on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("Experience Description"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Experience publish time"))

    tags = TaggableManager()

    def __str__(self):
        return f"{self.user} - {self.category}"


class ExperienceComment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(verbose_name=_("Comment"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Comment publish time"))

    def __str__(self):
        return f"{self.user} - {self.experience}"
