from rest_framework import serializers
from .models import Profile
from users_app.models import User
from users_app.serializers import UserSerializer
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model  =User
        fields = ('old_password', 'password', 'password2')


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password fields didn\'t match'})

        return attrs


    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Old password is not correct'})        

        return value


    def update(self, instance, validate_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validate_data['password'])
        instance.save()

        return instance  



class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
 
    class Meta:
        model = Profile
        fields = (
            'id',
            'name',
            'address',
            'profile',             #related_name
        )

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})    

        return value


    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})    

        return value


    def update(self, instance, validated_data):
    

        instance.name = validated_data['name'] 
        instance.address = validated_data['address'] 
        instance.email = validated_data['email'] 
        instance.phone = validated_data['phone']

        instance.save()

        return instance 
               


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email')
    phone = serializers.CharField(source='user.phone')


    class Meta:
        model = Profile
        depth = 1
        fields = ('user', 'id', 'username', 'email', 'name', 'phone', 'address')


    def update(self, instance, validated_data):
        # retrieve the User
        user_data = validated_data.pop('user', None)
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)

        # retrieve Profile
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()
        return instance               