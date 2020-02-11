# Cheetah starts behind bolt, 4 variables finish, distanceBolt, cheetahAcceleration, boltSpeed
import math
finish = int(input())
distancebolt = int(input())
cheetahAcc = int(input())
boltspeed = int(input())
timebolt = int(distancebolt/boltspeed)

distancecheetah = (2*(distancebolt + finish))
timecheetah = math.sqrt(distancecheetah/cheetahAcc)
#using acceleration formula1

if timebolt > timecheetah:
    print("Cheetah wins")

if timecheetah > timebolt:
    print("bolt wins")
if timecheetah == timebolt:
    print("A tie")
