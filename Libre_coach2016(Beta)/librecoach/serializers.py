from rest_framework import serializers
from .models import Stock, Annonce, User, Coach

#exemple pour la route
class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'

class AnnonceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annonce
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = '__all__'
