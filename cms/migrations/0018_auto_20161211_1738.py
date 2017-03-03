# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20161207_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliaspluginmodel',
            name='plugin',
            field=models.ForeignKey(related_name='alias_reference', editable=False, to='cms.CMSPlugin', null=True),
        ),
        migrations.AlterField(
            model_name='cmsplugin',
            name='parent',
            field=models.ForeignKey(blank=True, editable=False, to='cms.CMSPlugin', null=True),
        ),
    ]
