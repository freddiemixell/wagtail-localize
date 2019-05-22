# Generated by Django 2.1.7 on 2019-03-25 17:34

from django.conf import settings
from django.db import migrations

from wagtail_localize.compat import get_supported_language_variant


def initial_data(apps, schema_editor):
    Language = apps.get_model('wagtail_localize.Language')
    Region = apps.get_model('wagtail_localize.Region')
    Locale = apps.get_model('wagtail_localize.Locale')

    default_language, created = Language.objects.get_or_create(
        code=get_supported_language_variant(settings.LANGUAGE_CODE),
    )

    default_region = Region.objects.create(
        name='Default',
        slug='default',
        is_default=True,
    )

    default_region.languages.add(default_language)

    Locale.objects.create(
        language=default_language,
        region=default_region,
        is_active=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data, migrations.RunPython.noop)
    ]