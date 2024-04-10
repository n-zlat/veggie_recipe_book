from django.db import models


class MeasurementUnit(models.Model):
    MAX_UNIT_NAME_LENGTH = 50

    name = models.CharField(max_length=MAX_UNIT_NAME_LENGTH,
                            )

    def __str__(self):
        return self.name
