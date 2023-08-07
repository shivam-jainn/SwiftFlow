import uuid
from django.db import models
from registerform.models import SwiftUser
import json

class Ride(models.Model):
    rider = models.ForeignKey(SwiftUser, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(SwiftUser, on_delete=models.CASCADE, related_name='rides_as_driver')
    ride_id = models.UUIDField(default=uuid.uuid4)
    pickup_time = models.DateTimeField()
    pickup_loc = models.JSONField()
    drop_loc = models.JSONField()

    def set_pickup_location(self, latitude, longitude):
        self.pickup_loc = json.dumps({'latitude': latitude, 'longitude': longitude})

    def set_drop_location(self, latitude, longitude):
        self.drop_loc = json.dumps({'latitude': latitude, 'longitude': longitude})

    def get_pickup_latitude(self):
        return json.loads(self.pickup_loc).get('latitude')

    def get_pickup_longitude(self):
        return json.loads(self.pickup_loc).get('longitude')

    def get_drop_latitude(self):
        return json.loads(self.drop_loc).get('latitude')

    def get_drop_longitude(self):
        return json.loads(self.drop_loc).get('longitude')


class Message(models.Model):
    room = models.ForeignKey(Ride, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=300)
    time_sent = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(SwiftUser, on_delete=models.CASCADE, related_name='received_messages')
    sender = models.ForeignKey(SwiftUser, on_delete=models.CASCADE, related_name='sent_messages')
