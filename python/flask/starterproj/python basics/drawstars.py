def drawstars(myllist):
     for val in myllist:
         if type(val) is int:
             print
             for i in range(0,val,1):
                 print "*",
         elif type(val) is str:
             print
             strlen = len(val)
             for pfc in range (0,strlen,1):
                 print val[0].lower(),



mylist=[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawstars(mylist)
