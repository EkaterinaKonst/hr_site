from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Places(models.Model):
    country = models.CharField(max_length=30)
    company = models.ForeignKey(CommonInfo, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.country


class Department(models.Model):
    name_group = models.CharField(max_length=20)
    group_size = models.PositiveIntegerField(default=0)
    head_of_group = models.CharField(max_length=100)
    places = models.ManyToManyField(Places)

    def __str__(self):
        return f' {self.name_group} {self.head_of_group}'


class SubDepartment(models.Model):
    name_subgroup = models.CharField(max_length=20)
    subgroup_size = models.PositiveIntegerField(default=0)
    head_of_subgroup = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return f' {self.name_subgroup} {self.head_of_subgroup}'


class Employer(models.Model):
    empl_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_of_employment = models.DateField()
    salary = models.PositiveIntegerField(default=10000)
    boss = models.ForeignKey(SubDepartment, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f' {self.empl_name} {self.position} {self.date_of_employment} {self.salary} {self.boss}'
