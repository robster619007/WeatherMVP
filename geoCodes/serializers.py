from rest_framework import serializers
from .models import GeogInfo

class GeogInfoSerializer(serializers.Serializer):
    longitude = serializers.DecimalField( max_digits=22, decimal_places=16)
    latitude = serializers.DecimalField( max_digits=22, decimal_places=16)
    timezone = serializers.CharField(max_length=150)
    current_date = serializers.DateField()
    current_sunrise = serializers.DateField()
    current_sunset = serializers.DateField()
    current_temp = serializers.DecimalField(max_digits=5,decimal_places=3)

    def create(self,validated_data):
        return GeogInfo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.GeogCode_id = validated_data.get('GeogCode_id',instance.GeogCode_id)
        instance.longitude = validated_data.get('longitude',instance.longitude)
        instance.latitude = validated_data.get('latitude',instance.latitude)
        instance.timezone = validated_data.get('timezone',instance.timezone)
        instance.current_date = validated_data.get('current_date',instance.current_date)
        instance.current_sunrise = validated_data.get('current_sunrise',instance.current_sunrise)
        instance.current_sunset = validated_data.get('current_sunset',instance.current_sunset)
        instance.current_temp = validated_data.get('current_temp',instance.current_temp)
        instance.save()
        return instance