class TowerOfHanoi:
    def move(self,n, f,t,i):

        if n == 1:
            print ("moved %s from %s to %s" %(str(n),str(f),str(t)))
            return
        self.move(n-1,f,i,t)
        print ("moved %s from %s to %s" %(str(n),str(f),str(t)))
        self.move(n-1,i,t,f)


toh = TowerOfHanoi()

toh.move(6,'A','C','B')
