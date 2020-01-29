from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    firstName = serializers.CharField(max_length = 30)
    lastName = serializers.CharField(max_length = 30)
    createdDate = serializers.DateTimeField()