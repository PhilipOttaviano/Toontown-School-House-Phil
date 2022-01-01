from otp.otpbase import OTPGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import ToontownGlobals
from toontown.battle import SuitBattleGlobals
from toontown.coghq import CogDisguiseGlobals
import random
from toontown.toon import NPCToons
import copy, string
from toontown.hood import ZoneUtil
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
import time, types, random
notify = DirectNotifyGlobal.directNotify.newCategory('TaskForce')

class TaskForceQuest:
    
    def __init__(self, neededCogs=0, neededCogTypes=[], neededCogBuildings=0, buildingType='s', neededVps=0, rewardId=0, reward=0):
        self.neededCogs = neededCogs
        self.neededCogTypes = neededCogTypes
        self.neededCogBuildings = neededCogBuildings
        self.buildingType = buildingType
        self.neededVps = neededVps
        self.rewardId = rewardId
        self.reward = reward

    def check(self, cond, msg):
        pass

    def checkNumCogs(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def getNeededCogs(self):
        return self.checkNumCogs(self.neededCogs)
    
    def setNeededCogs(self, neededCogs):
        self.neededCogs = neededCogs
    
    def getNeededCogTypes(self):
        return self.neededCogTypes
    
    def getNeededCogBuildings(self):
        return self.neededCogBuildings
    
    def getBuildingType(self):
        return self.buildingType
    
    def getRewardId(self):
        return self.rewardId
    
    def getReward(self):
        return self.reward
    
    def setRewardId(self, rewardId):
        self.rewardId = rewardId
    
    def setReward(self, reward):
        self.reward = reward
    
    def getNeededVps(self):
        return self.neededVps
    
    def setNeededVps(self, neededVps):
        self.neededVps = neededVps

TaskForceDict = TaskForceQuest(2, None, 0, 0, 0, 0, 0)


    

    