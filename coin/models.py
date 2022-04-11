from django.db import models

from user.models import CustomUser

class Coin(models.Model):
    name = models.CharField(max_length=255, unique=True)
    verbose_name = models.CharField(max_length=255, unique=True)


class PricePredictionResult(models.Model):
    price = models.PositiveBigIntegerField()
    branches_total_coins = models.TextField() # hold all coins put on each branch by all players


class PricePrediction(models.Model):
    user = models.ForeignKey(
                to=CustomUser,
                on_delete=models.SET_NULL,
                related_name='price_predictions',
                null=True,
                db_index=True
            )
    coin = models.ForeignKey(to=Coin,
                on_delete=models.SET_NULL,
                related_name='price_predictions',
                null=True,
                db_index=True
            )
    prediction = models.TextField() # holds branch values in json format
    predicted_at = models.DateTimeField(auto_now=True, editable=False)
    result = models.ForeignKey(to=PricePredictionResult,
                on_delete=models.SET_NULL,
                related_name='price_predictions',
                null=True,
                db_index=True
            )


class PricePredictionParam(models.Model):
    coin = models.ForeignKey(
                to=Coin,
                on_delete=models.SET_NULL,
                related_name='price_prediction_params',
                null=True,
                db_index=True
            )
    start_at = models.DateTimeField(editable=False)
    end_at = models.DateTimeField(editable=False)
    eval_time = models.DateTimeField(editable=False, db_index=True)
    m = models.PositiveIntegerField()
    n = models.PositiveIntegerField()
    branches = models.TextField()
