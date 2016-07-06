from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django import forms
from mptt.admin import MPTTModelAdmin
from django.utils.translation import ugettext_lazy as _

from cflatpages.models import CFlatPage, Category

if 'ckeditor' in settings.INSTALLED_APPS:
    from ckeditor.widgets import CKEditorWidget


class CategorizedFlatpageForm(FlatpageForm):
    """
    The form for the CategorizedFlatPage model
    """
    content = forms.CharField(widget=CKEditorWidget()
        if 'ckeditor' in settings.INSTALLED_APPS else forms.TextInput())

    class Meta:
        model = CFlatPage
        fields = '__all__'


@admin.register(CFlatPage)
class CategorizedFlatPageAdmin(FlatPageAdmin):
    """
    Management of the CategorizedFlatPage model
    """
    form = CategorizedFlatpageForm
    list_display = ['title', 'url', 'category', 'num']
    fieldsets = (
        (None, {
            'fields': (
                'category',
                'url',
                'title',
                'content',
                'sites',
                'keywords',
                'description',
                'num', )}),
        (
            _(u'advanced options'),
            {
                'classes': ('collapse',),
                'fields': (
                    'enable_comments',
                    'registration_required',
                    'template_name', ), }, ), )


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    pass

admin.site.unregister(FlatPage)
