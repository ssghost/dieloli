from script.Core import CacheContorl,TextLoading,EraPrint,PyCmd
from script.Design import GameTime,CmdButtonQueue

# 用于查看当前场景的面板
def seeScenePanel():
    sceneData = CacheContorl.sceneData.copy()
    titleText = TextLoading.getTextData(TextLoading.stageWordPath,'75')
    EraPrint.plt(titleText)
    timeText = GameTime.getDateText()
    EraPrint.p(timeText)
    EraPrint.p(' ')
    sceneId = CacheContorl.playObject['object']['0']['Position']
    sceneName = sceneData['SceneData'][sceneId]['SceneName']
    sceneInfoHead = TextLoading.getTextData(TextLoading.stageWordPath, '76')
    sceneInfo = sceneInfoHead + sceneName
    EraPrint.p(sceneInfo)
    EraPrint.plittleline()

# 用于查看当前场景上角色列表的面板
def seeScenePlayerListPanel():
    inputS = []
    sceneData = CacheContorl.sceneData.copy()
    seePlayerText = TextLoading.getTextData(TextLoading.messagePath,'26')
    EraPrint.p(seePlayerText)
    EraPrint.p('\n')
    sceneId = CacheContorl.playObject['object']['0']['Position']
    scenePlayerList = sceneData['ScenePlayerData'][sceneId]
    nowScenePlayerList = scenePlayerList.copy()
    nowScenePlayerList.remove('0')
    for playerId in nowScenePlayerList:
        playerName = CacheContorl.playObject['object'][str(playerId)]['Name']
        PyCmd.pcmd(playerName, playerName, None)
        inputS.append(playerName)
        EraPrint.p(' ')
    EraPrint.plittleline()
    return inputS

# 用于查看对象信息的面板
def seeObjectInfoPanel():
    objectInfo = TextLoading.getTextData(TextLoading.stageWordPath, '77')
    EraPrint.p(objectInfo)
    objectId = CacheContorl.playObject['objectId']
    objectData = CacheContorl.playObject['object'][objectId]
    objectName = objectData['Name']
    EraPrint.p(objectName)
    EraPrint.p(' ')
    intimateInfo = TextLoading.getTextData(TextLoading.stageWordPath,'16')
    gracesInfo = TextLoading.getTextData(TextLoading.stageWordPath,'17')
    objectIntimate = objectData['Intimate']
    objectGraces = objectData['Graces']
    objectIntimateText = intimateInfo + objectIntimate
    objectGracesText = gracesInfo + objectGraces
    EraPrint.p(objectIntimateText)
    EraPrint.p(' ')
    EraPrint.p(objectGracesText)
    EraPrint.plittleline()

def inSceneButtonPanel():
    inputs = CmdButtonQueue.optionint(cmdList=CmdButtonQueue.inscenelist1, cmdColumn=9, askfor=False, cmdSize='center')
    EraPrint.plittleline()
    return inputs
