from obswebsocket import requests, obsws
from math import sin, cos, pi

# Change this to your websocket password and port - default 4455
password = "aaaaaa"
port = 4455

ws = obsws(port=port, password=password)
ws.connect()

# Edit these to choose an object
scene_name = "Scene"
object_name = "Display Capture"

monitorId = print(ws.call(requests.GetSceneItemId(sceneName=scene_name, sourceName=object_name)))
transform = {"rotation": 0, "positionX": 0, "positionY": 0}

# These are the variables that you can edit to change how the object rotates
length=1920
height=1080
rotationSpeed = .01
revolutions = 10000

rotation = 0
rotationCount = 0

transform["rotation"] = rotation

radianConversion = pi/180

def setxypos():
    global transform
    transform["positionX"] = length / 2 - (length * cos(rotation * radianConversion))/2 + (height * sin(rotation * radianConversion))/2
    transform["positionY"] = height/2 - (length * sin(rotation * radianConversion))/2 - (height * cos(rotation * radianConversion))/2
    transform["rotation"] = rotation

for i in range(int((360 * revolutions) / rotationSpeed)):
    if rotation > 360:
        rotation = rotation - 360
        rotationCount += 1
    setxypos()
    ws.call(requests.SetSceneItemTransform(sceneName="Scene", sceneItemId=1, sceneItemTransform=transform))
    rotation += rotationSpeed
