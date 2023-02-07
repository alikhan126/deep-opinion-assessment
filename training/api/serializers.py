from rest_framework import serializers

from training.models import Tag, TrainingData


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TrainingDataListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = TrainingData
        fields = "__all__"


class TrainingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingData
        fields = "__all__"


class TrainingDataTagSerializer(serializers.Serializer):
    text = serializers.CharField()
    tags = serializers.ListField(child=TagSerializer(), required=False)

    def create(self, validated_data):
        text = validated_data["text"]
        training_data = TrainingData(text=text)
        training_data.save()

        # Add tags to data
        tags = validated_data.get("tags")
        tag_ids = [
            Tag.objects.create(
                aspect=tag.get("aspect"), sentiment=tag.get("sentiment")
            ).id
            for tag in tags
        ]

        training_data.tags.add(*tag_ids)

        return training_data


class TrainingDataUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ("file",)
