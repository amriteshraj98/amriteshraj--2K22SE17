from django.db import models
from django.contrib.auth.models import User

class Recognition(models.Model):
    sender = models.ForeignKey(User, related_name="sent_recognitions", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_recognitions", on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} recognized {self.receiver.username} with {self.credits} credits"

class Endorsement(models.Model):
    recognition = models.ForeignKey(Recognition, related_name="endorsements", on_delete=models.CASCADE)
    endorser = models.ForeignKey(User, related_name="endorsements", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.endorser.username} endorsed recognition {self.recognition.id}"

class Redemption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credits_redeemed = models.PositiveIntegerField()
    voucher_value = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} redeemed {self.credits_redeemed} credits"
