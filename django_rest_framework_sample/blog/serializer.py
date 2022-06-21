from attr import fields
from rest_framework import serializers
from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meata:
        model = User
        fields = ('id', 'name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    author = UserSerializer(read_only=True)

    class Meta:
        model = Entry
        fields = ('id', 'title', 'body', 'created_at', 'status', 'author')
