from django.db import models


class Result(models.Model):
    result = models.CharField(max_length=20)

    def __str__(self):
        return self.result


class TestItem(models.Model):
    test_item = models.CharField(max_length=20)

    def __str__(self):
        return self.test_item


class Test1(models.Model):
    test_name = models.ForeignKey(TestItem, unique=True, on_delete=models.CASCADE)
    test_result = models.ForeignKey(Result, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Test2(models.Model):
    test_name = models.ForeignKey(TestItem, unique=True, on_delete=models.CASCADE)
    test_result = models.ForeignKey(Result, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Test3(models.Model):
    test_name = models.ForeignKey(TestItem, unique=True, on_delete=models.CASCADE)
    test_result = models.ForeignKey(Result, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Patient(models.Model):
    patient_id = models.CharField(unique=True, max_length=10)
    patient_name = models.CharField(max_length=20)
    patient_pathology_number = models.CharField(max_length=10)
    patient_hospital_number = models.CharField(max_length=10)
    patient_test_1 = models.ForeignKey(Test1, on_delete=models.CASCADE)
    patient_test_2 = models.ForeignKey(Test2, on_delete=models.CASCADE)
    patient_test_3 = models.ForeignKey(Test3, on_delete=models.CASCADE)
    patient_note = models.CharField(max_length=200)

    def __str__(self):
        return self.patient_name







