import json
from lib.umqtt.simple import MQTTClient
from conf.conf import MQTT_TOPIC_NAME, MQTT_BROKER_URL, DEVICE_UUID


class Mqtt:
    client = MQTTClient(client_id=DEVICE_UUID, server=MQTT_BROKER_URL, port=1883)
    message_queue = None
    def connect_to_broker(self):
        try:
            self.client.connect()
            return "connected"
        except Exception as e:
            print("connect to broker error", e)
            return "disconnected"

    def subscribe_to_topic(self, topic_name, message_queue):
        try:
            self.message_queue = message_queue
            self.client.set_callback(self.sub_cb)
            self.client.subscribe(topic_name)
            return topic_name
        except Exception as e:
            print("subscribe to topic error", e)
            return "none"

    def sub_cb(self, topic, msg):
        msg = msg.decode('utf8').replace("'", '"')
        msg = json.loads(msg)
        if "all" in msg['targets'] or DEVICE_UUID in msg["targets"]:
            self.message_queue.append(msg)
    