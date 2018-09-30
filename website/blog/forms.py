from django import forms
from .models import Blogpost


class BlogpostForm(forms.ModelForm):
    """
    Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table)
    or human-readable singular and plural names (verbose_name and verbose_name_plural). None are required,
    and adding class Meta to a model is completely optional.
    https://docs.djangoproject.com/en/dev/ref/models/options/
    """
    class Meta:
        """
           ``fields`` is an optional list of field names. If provided, include only
           the named fields in the returned fields. If omitted or '__all__', use all
           fields.
           """
        model = Blogpost
        fields = ['title', 'author', 'body', 'published']


