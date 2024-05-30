from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Profile, Interest, Schedule, Platform, LFGAlert#, Gender


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'name']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'free']

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name']

class ProfileSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(many=True)
    schedule = ScheduleSerializer(many=True)
    platform = PlatformSerializer(many=True)

    class Meta:
        model = Profile
        exclude = ('coin_balance',)
        extra_kwargs = {"username": {"write_only": True}}

    def create(self, validated_data):
        interest_data = validated_data.pop('interest')
        schedule_data = validated_data.pop('schedule')
        platform_data = validated_data.pop('platform')

        profile = Profile.objects.create(**validated_data)

        for data in interest_data:
            interest, created = Interest.objects.get_or_create(**data)
            profile.interest.add(interest)

        for data in schedule_data:
            schedule, created = Schedule.objects.get_or_create(**data)
            profile.schedule.add(schedule)

        for data in platform_data:
            platform, created = Platform.objects.get_or_create(**data)
            profile.platform.add(platform)

        return profile
    
    def update(self, instance, validated_data):
        interest_data = validated_data.pop('interest')
        schedule_data = validated_data.pop('schedule')
        platform_data = validated_data.pop('platform')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gamer_tag = validated_data.get('gamer_tag', instance.gamer_tag)
        instance.display_gamer_tag = validated_data.get('display_gamer_tag', instance.display_gamer_tag)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.radius = validated_data.get('radius', instance.radius)
        instance.save()

        instance.interest.clear()
        for data in interest_data:
            interest, created = Interest.objects.get_or_create(**data)
            instance.interest.add(interest)

        instance.schedule.clear()
        for data in schedule_data:
            schedule, created = Schedule.objects.get_or_create(**data)
            instance.schedule.add(schedule)

        instance.platform.clear()
        for data in platform_data:
            platform, created = Platform.objects.get_or_create(**data)
            instance.platform.add(platform)

        return instance


class LFGAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = LFGAlert
        fields = '__all__'






""" class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = '__all__'
        exclude = ('coin_balance',)
        extra_kwargs = {"username": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        profile = Profile.objects.create(**validated_data)
        return profile """










class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}