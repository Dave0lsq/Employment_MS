from django.db import models

class Department(models.Model):
    '''Department Table'''
    title = models.CharField(verbose_name='Department Title', max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    '''Employee Table'''
    name = models.CharField(verbose_name='Name', max_length=16)
    password = models.CharField(verbose_name='Password', max_length=64)
    age = models.IntegerField(verbose_name='Age')
    balance = models.DecimalField(verbose_name='Balance', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='Onboarding Date')

    # - to, associate with the other table
    # - to_field, associate the specific column
    #   Foreign Keys with Cascade Delete
    depart = models.ForeignKey(verbose_name='Department', to='Department', to_field='id', on_delete=models.CASCADE)
    # Or set NULL
    #depart = models.ForeignKey(to='Department', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)

    gender_choices = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )

    gender = models.SmallIntegerField(verbose_name='Gender', choices=gender_choices)


class SchoolInfo(models.Model):
    name = models.CharField(verbose_name='School Name', max_length=64)

    district_choices = (
        (1, 'Wan Chai'),
        (2, 'Central and Western'),
        (3, 'Sai Kung'),
        (4, 'Eastern'),
        (5, 'Southern'),
        (6, 'Tsuen Wan'),
        (7, 'North'),
        (8, 'Kowloon City'),
        (9, 'Yau Tsim Mong'),
        (10, 'Sha Tin'),
        (11, 'Islands'),
        (12, 'Yuen Long'),
        (13, 'Tai Po'),
        (14, 'Wong Tai Sin'),
        (15, 'Tuen Mun'),
        (16, 'Kwai Tsing'),
        (17, 'Sham Shui Po'),
        (18, 'Kwun Tong'),
    )
    district = models.SmallIntegerField(verbose_name='District', choices=district_choices)

    status_choices = (
        (0, 'Not Promoted'),
        (1, 'Promoted'),
    )
    status = models.SmallIntegerField(verbose_name='Status', choices=status_choices)