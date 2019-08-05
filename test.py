import Leap, sys, thread, time, Sample_module

def main():
   listenerA = Sample_module.SampleListener()
   listenerB = Sample_module.SampleListener()
   controller = Leap.Controller()

   listenerA.on_init(controller)
   listenerA.on_connect(controller)
   while True:
      try:
         listenerA.on_frame(controller)
         palmA = listenerA.plst
         boneA = listenerA.boneZ
         if len(palmA) > 0:
            if abs(palmA[2]-boneA)>=40:
               print "Bba"
               while True:
                  listenerB.on_frame(controller)
                  palmB = listenerB.plst
                  boneB = listenerB.boneZ
                  if len(palmB) > 0:
                     vector = []
                     for i in range(len(palmA)):
                        vector.append(abs(palmB[i]-palmA[i]))

                     index = 3
                     if max(vector) >= 100:
                        index = vector.index(max(vector))

                     if index == 0:
                        if palmB[0] - palmA[0] > 0:
                           print "right"
                        else:
                           print "left"
                     elif index == 1:
                        if palmB[1] - palmA[1] > 0:
                           print "up"
                        else:
                           print "down"
                     elif index == 2:
                        if palmB[2] - palmA[2] > 0:
                           print "back"
                        else:
                           print "front"
                     else:
                        print "stop"
                        if abs(palmB[2] - boneB) < 40:
                           print "Muk"
                           break
                     del palmB[:]
         
            elif abs(palmA[2]-boneA)<40:
               print "Muk"
               del palmA[:]
      except KeyboardInterrupt:
         break

   

main()
