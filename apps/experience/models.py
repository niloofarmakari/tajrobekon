from django.contrib.auth import get_user_model
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExperienceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))
    slug = models.SlugField(max_length=100, primary_key=True)
    description = models.TextField(default="", blank=True, verbose_name=_("Category Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Experience publish time"))

    def __str__(self):
        return self.name

    def get_schema(self):
        """Get schema for https://schema.org/Thing"""
        return {
            "@context": "http://schema.org",
            "@type": "Thing",
            "alternateName": self.name,
            "description": self.description,
            "identifier": self.slug,
        }

    class Meta:
        verbose_name = _("Experience Category")
        verbose_name_plural = _("Experience Categories")


class Experience(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(ExperienceCategory, verbose_name=_("Experience Category"), on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("Experience Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Experience publish time"))

    def __str__(self):
        return f"{self.user} - {self.category}"

    def get_schema(self):
        """Get schema for https://schema.org/Quotation"""
        return {
            "@context": "http://schema.org",
            "@type": "Quotation",
            "author": self.user.get_schema(),
            "about": self.category.get_schema(),
            "comment": [comment.get_schema() for comment in self.comments.all()],
        }

    def get_similar(self):
        return (
            Experience.objects.annotate(
                rank=SearchRank(
                    SearchVector("description", "category__name", "category__slug"), SearchQuery(self.description)
                )
            )
            .filter(rank__gt=0.001)
            .exclude(id=self.id)
            .order_by("-rank")[:5]
        )

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")
        ordering = ["-created_at"]


class ExperienceComment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(verbose_name=_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Comment publish time"))

    def __str__(self):
        return f"{self.user} - {self.experience}"

    def get_schema(self):
        """Get schema for https://schema.org/UserComments"""
        return {
            "@context": "http://schema.org",
            "@type": "Comment",
            "creator": self.user.get_schema(),
            "commentText": self.comment,
            "commentTime": self.created_at.date().strftime("%Y-%m-%d"),
        }

    class Meta:
        verbose_name = _("Experience Comment")
        verbose_name_plural = _("Experience Comments")
        ordering = ["-created_at"]
