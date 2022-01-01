from direct.directnotify import DirectNotifyGlobal

from toontown.taskforce import TaskForce

class TaskForceManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('TaskForceManagerAI')
    
    def __init__(self, air):
        self.air = air
    
    def getCogsNeeded(self, toon, suitsKilled):
        self.toonsTasks = toon.getTaskForceQuests()
        
        for task in self.toonsTasks:
            for suit in suitsKilled:
                self.cogsNeeded = TaskForce.TaskForceDict.getNeededCogs()
                TaskForce.TaskForceDict.setNeededCogs(self.cogsNeeded - 1)
                print("Cogs needed: " + str(self.cogsNeeded))
                if self.cogsNeeded < 1:
                    print('Toon has completed a task force quest!')


                
        
        