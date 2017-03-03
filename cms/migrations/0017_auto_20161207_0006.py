# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
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
