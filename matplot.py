import matplotlib.pyplot as plt
import numpy as np

import paho.mqtt.client as mqtt

# define callback functions for different MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# create an MQTT client instance
client = mqtt.Client()

# assign callback functions to client events
client.on_connect = on_connect
client.on_message = on_message

# connect to MQTT broker
client.connect("broker.hivemq.com", 1883, 60)

# start the MQTT loop
client.loop_start()

# publish a message to the "topic/test" topic
client.publish("topic/test", "Hello, world!")

# wait for messages
while True:
    pass

# stop the MQTT loop
client.loop_stop()

# Generate some data
##x = np.linspace(0, 10, 100)
##y = np.sin(x)
##
### Create a figure and axis object
##fig, ax = plt.subplots()
##
### Plot the data
##ax.plot(x, y)
##
### Add some labels and a title
##ax.set_xlabel('x')
##ax.set_ylabel('sin(x)')
##ax.set_title('A Simple Line Plot')
##
### Show the plot
##plt.show()

