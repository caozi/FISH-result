from django.db import models


class Result(models.Model):
    result = models.CharField(max_length=20)

    def __str__(self):
        return self.result


class Item(models.Model):
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.item


class Patient(models.Model):
    patient_id = models.CharField(unique=True, max_length=10)
    patient_name = models.CharField(max_length=20)
    patient_number = models.CharField(max_length=10)
    patient_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    patient_result = models.ForeignKey(Result, on_delete=models.CASCADE)
    patient_note = models.CharField(max_length=200)

    def __str__(self):
        return self.patient_id







