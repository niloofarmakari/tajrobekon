# Tajrobe Kon (Experience Sharing Platform)

You can share your personal experiences and learn from others.

## Technical features

-   Django 3.2
-   Using [Poetry](https://github.com/python-poetry/poetry) for dependency management.
-   Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
-   Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
-   Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).

## Commands

Commands for development

### Make Messages (Generate Translation Files)

```
django-admin makemessages -l fa -e txt,py,html --no-location
```

### Compile Messages

```
django-admin compilemessages -l fa
```
