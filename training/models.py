from django.db import models


class Tag(models.Model):
    POS = "POS"
    NEG = "NEG"
    NEU = "NEU"

    SENTIMENT_CHOICES = (
        (POS, "POS"),
        (NEG, "NEG"),
        (NEU, "NEU"),
    )
    aspect = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=3, choices=SENTIMENT_CHOICES)

    def __str__(self):
        return f"aspect: {self.aspect}, sentiment: {self.sentiment}"


class TrainingData(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.text
