from django.db import models

class d_type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.type_name}"

class drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    drug_name = models.CharField(max_length=255)
    drug_type = models.ForeignKey(d_type, on_delete=models.CASCADE)
    drug_qty = models.IntegerField()
    drug_exp = models.DateField()
    def __str__(self):
        return f"{self.drug_name} , {self.drug_exp}"