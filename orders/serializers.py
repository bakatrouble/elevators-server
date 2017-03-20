from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'application', 'number', 'date', 'to_date', 'act_date', 'controller', 'manager', 'expert',
                  'head_specialist', 'specialists',)
