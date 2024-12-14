import zope.interface as zi
from .Interfaces.IRepository import IRepository

@zi.implementer(IRepository)
class RepositoryBase:
    def __init__(self, model):
        self.model = model
        
    def add(self, record):
        return self.model.objects.create(**record)
    
    def getAll(self):
        return self.model.objects.all()
    
    def remove(self, record_id):
        return self.model.objects.filter(id=record_id).delete()