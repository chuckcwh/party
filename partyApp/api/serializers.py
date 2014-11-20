from django.http import request
from rest_framework import serializers
from partyApp.models import Party, Profile


class ProfileSerializer(serializers.ModelSerializer):
    party_host = serializers.SerializerMethodField('get_party_host')
    party_attend = serializers.SerializerMethodField('get_party_attend')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'password', 'email', 'sex', 'first_name', 'last_name', 'birth', 'sex', 'about', 'image', 'party_host', 'party_attend')
        write_only_fields = ('password',)

    def get_party_host(self, obj):
        return Party.objects.filter(owner=obj).values()

    def get_party_attend(self, obj):
        return Party.objects.filter(participants=obj).values()


class PartySerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField('get_participants')
    # project_count = serializers.SerializerMethodField('get_project_count')
    # project_follow_count = serializers.SerializerMethodField('get_project_follow_count')
    owner = ProfileSerializer(read_only=True)

    class Meta:
        model = Party
        fields = ('id', 'title', 'latitude', 'longitude', 'time', 'maxPpl','minAge', 'maxAge', 'targetSex', 'owner', 'partyImage', 'participants')
        # read_only_fields = ('date_joined',)

    def get_participants(self, obj):
        return Profile.objects.filter(parties_participants=obj).values()
    # def get_project_count(self, obj):
    #     return obj.project.count()
    #

    #
    # def get_project_follow_count(self, obj):
    #     return Project.objects.filter(follower=obj).count()

    # username should be >= 4 digits
    # def validate_username(self, attrs, source):
    #     username = attrs[source]
    #     if len(username) < 4:
    #         raise serializers.ValidationError('Username is too short! (>= 4 digits)')
    #     return attrs

