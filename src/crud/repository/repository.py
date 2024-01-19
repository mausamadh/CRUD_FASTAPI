
from src.entrypoint.database import data

class InMemoryRep:
    def __init__(self):
        self.repo=data

    def add(self,item):
        self.repo.append(item)
        return "added successfully"

    def update(self,index,change):
        self.repo[index]=change
        return "updated successfully"
    
    def get(self,index):
        return self.repo[index]
    
    def delete(self,index):
        return self.repo.pop(index)

repo=InMemoryRep