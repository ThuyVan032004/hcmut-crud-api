import zope.interface as zi

class IRepository(zi.Interface):
    def add(self, entity):
        pass
    
    def getAll(self):
        pass 
    
    def update(self, entity):
        pass
    
    def remove(self, entity):
        pass

