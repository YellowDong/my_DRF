from django.db import models

# Create your models here.


class IpoInfo(models.Model):
    security_code = models.CharField(primary_key=True, max_length=10)
    security_name = models.CharField(max_length=20, blank=True, null=True)
    total_initial_issue = models.IntegerField(blank=True, null=True)
    actual_fundraised = models.FloatField(blank=True, null=True)
    offline_issue_date = models.DateField(blank=True, null=True)
    online_issue_date = models.DateField(blank=True, null=True)
    issue_price = models.FloatField(blank=True, null=True)
    total_issued = models.FloatField(blank=True, null=True)
    ipo_pe_ratio = models.FloatField(blank=True, null=True)
    offline_circulation = models.FloatField(blank=True, null=True)
    online_circulation = models.FloatField(blank=True, null=True)
    online_purchase_limit = models.FloatField(blank=True, null=True)
    success_rate = models.CharField(max_length=50, blank=True, null=True)
    success_rate_date = models.DateField(blank=True, null=True)
    listed_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    payment_end_date = models.DateField(blank=True, null=True)
    crawl_timestamp = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipo_info'

