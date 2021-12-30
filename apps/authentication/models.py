from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_schema(self):
        """Get schema for https://schema.org/Person"""
        return {
            "@context": "http://schema.org",
            "@type": "Person",
            "givenName": self.first_name,
            "familyName": self.last_name,
            "email": self.email,
        }
