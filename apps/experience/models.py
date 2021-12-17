from django.db import models
from django.utils.translation import gettext_lazy as _


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
    name = models.CharField(
        max_length=100,
        verbose_name=_("Category Name"),
    )
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(
        default="",
        blank=True,
        verbose_name=_("Category Description"),
    )
    # image = models.ImageField(upload_to="experience/category/", blank=True, verbose_name=_("Category Image"))

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
    author_name = models.CharField(max_length=100, verbose_name=_("Author Name"))
    category = models.ForeignKey(ExperienceCategory, verbose_name=_("Experience Category"), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=_("Experience Title"))
    subtitle = models.CharField(max_length=100, blank=True, default="", verbose_name=_("Experience Subtitle"))
    description = models.TextField(verbose_name=_("Experience Description"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Experience publish time"))
    # image = models.ImageField(upload_to="experience/images/", blank=True, verbose_name=_("Experience Image"))

    def __str__(self):
        return self.title
