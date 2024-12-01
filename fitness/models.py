from django.contrib.auth.models import User
from django.db import models
from datetime import date, timedelta

class StepEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    steps = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def tier(self):
        """Determine tier based on daily steps."""
        if self.steps >= 5000:
            return 'Gold'
        elif self.steps >= 4000:
            return 'Silver'
        elif self.steps >= 3000:
            return 'Bronze'
        return 'None'

class WeeklyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start_date = models.DateField()
    days_met = models.PositiveIntegerField(default=0)
    tier = models.CharField(max_length=10, choices=[
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Bronze', 'Bronze'),
        ('None', 'None'),
    ])
    points = models.PositiveIntegerField(default=0)

    def calculate_points(self):
        """Assign points based on the tier."""
        if self.tier == 'Gold':
            return 5 + 3
        elif self.tier == 'Silver':
            return 5 + 2
        elif self.tier == 'Bronze':
            return 5 + 1
        return 0

class MonthlyJackpot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    tier = models.CharField(max_length=10)
    prize_amount = models.PositiveIntegerField()
