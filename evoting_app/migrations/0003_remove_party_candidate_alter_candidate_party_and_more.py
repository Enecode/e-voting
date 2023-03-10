# Generated by Django 4.1.7 on 2023-03-12 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evoting_app', '0002_remove_voter_voter_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='candidate',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='evoting_app.party'),
        ),
        migrations.AlterField(
            model_name='result',
            name='winning_party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='evoting_app.party'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='voter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verifications', to='evoting_app.voter'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to='evoting_app.party'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to='evoting_app.voter'),
        ),
    ]
