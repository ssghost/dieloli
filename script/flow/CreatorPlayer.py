import core.EraPrint as eprint
import script.TextLoading as textload
import core.game as game
import core.CacheContorl as cache
import script.Ans as ans
import core.PyCmd as pycmd
import random
import script.AttrCalculation as attr

playerId = '0'

def inputName_func():
    cache.playObject['objectId'] = playerId
    cache.playObject['object'][playerId] = cache.temporaryObject.copy()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('4'))
    yrn = ans.optionint(ans.currencymenu,1)
    eprint.p('\n')
    if yrn == 0:
        pycmd.clr_cmd()
        inputNickName_func()
        return
    elif yrn == 1:
        pycmd.clr_cmd()
        eprint.pline()
        eprint.pl(textload.loadMessageAdv('3'))
        playerName = game.askfor_str()
        eprint.pl(playerName)
        eprint.p('\n')
        cache.temporaryObject['Name'] = playerName
        pycmd.clr_cmd()
        inputName_func()
    elif yrn == 2:
        cache.wframeMouse['wFrameRePrint'] = 1
        eprint.pnextscreen()
        import script.mainflow as mainflow
        mainflow.main_func()
    pass

def inputNickName_func():
    cache.playObject['object'][playerId] = cache.temporaryObject.copy()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('6'))
    yrn = ans.optionint(ans.inputnickname,1)
    eprint.p('\n')
    if yrn == 0:
        pycmd.clr_cmd()
        inputSexConfirm_func()
    elif yrn == 1:
        pycmd.clr_cmd()
        eprint.pline()
        eprint.pl(textload.loadMessageAdv('5'))
        playerNickName = game.askfor_str()
        eprint.pl(playerNickName)
        eprint.p('\n')
        cache.temporaryObject['NickName'] = playerNickName
        pycmd.clr_cmd()
        inputNickName_func()
    elif yrn == 2:
        pycmd.clr_cmd()
        cache.temporaryObject['NickName'] = cache.temporaryObject['Name']
        inputNickName_func()
    elif yrn == 3:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputName_func()
    pass

def inputSexConfirm_func():
    pycmd.clr_cmd()
    sexId = cache.playObject['object'][playerId]['Sex']
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('8')[sexId])
    yrn = ans.optionint(ans.currencymenu,1)
    eprint.p('\n')
    if yrn == 0:
        if sexId == textload.loadRoleAtrText('Sex')[2]:
            cache.temporaryObject['Features']['Sex'] = textload.loadRoleAtrText('Features')['Sex'][0]
        elif sexId == textload.loadRoleAtrText('Sex')[3]:
            cache.temporaryObject['Features']['Sex'] = textload.loadRoleAtrText('Features')['Sex'][1]
        pycmd.clr_cmd()
        attributeGenerationBranch_func()
    elif yrn == 1:
        pycmd.clr_cmd()
        inputSexChoice_func()
    elif yrn == 2:
        pycmd.clr_cmd()
        inputNickName_func()
    pass

def inputSexChoice_func():
    pycmd.clr_cmd()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('7'))
    yrn = ans.optionint(ans.sexmenu,1)
    eprint.p('\n')
    sex = textload.loadRoleAtrText('Sex')
    sexMax = len(sex) - 1
    if yrn in range(0,sexMax):
        sexAtr = sex[yrn]
        cache.temporaryObject['Sex'] = sexAtr
        cache.playObject['object'][playerId] = cache.temporaryObject.copy()
        pycmd.clr_cmd()
        inputSexConfirm_func()
    elif yrn == 4:
        rand = random.randint(0, len(sex) - 1)
        sexAtr = sex[rand]
        cache.temporaryObject['Sex'] = sexAtr
        cache.playObject['object'][playerId] = cache.temporaryObject.copy()
        pycmd.clr_cmd()
        inputSexConfirm_func()
    elif yrn == 5:
        pycmd.clr_cmd()
        eprint.p('\n')
        inputSexConfirm_func()
    pass

def attributeGenerationBranch_func():
    pycmd.clr_cmd()
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('9'))
    yrn = ans.optionint(ans.currencymenu,1)
    if yrn == 0:
        pycmd.clr_cmd()
        detailedSetting_func1()
    elif yrn == 1:
        pycmd.clr_cmd()
        playerSex = cache.playObject['object']['0']['Sex']
        temlist = attr.getTemList()
        temId = temlist[playerSex]
        temData = attr.getAttr(temId)
        cache.temporaryObject['Age'] = temData['Age']
        acknowledgmentAttribute_func()
    elif yrn == 2:
        pycmd.clr_cmd()
        inputSexConfirm_func()
    pass

def detailedSetting_func1():
    eprint.p('\n')
    eprint.pline()
    playerSex = cache.playObject['object']['0']['Sex']
    sexList = textload.loadRoleAtrText('Sex')
    featuresList = attr.getFeaturesList()
    eprint.pl(textload.loadMessageAdv('10'))
    yrn = ans.optionint(ans.detailedsetting1,1)
    if yrn == 0:
        pycmd.clr_cmd()
        detailedSetting_func2()
    elif yrn == 1:
        if playerSex == sexList[0]:
            cache.featuresList['Age'] = featuresList["Age"][0]
        elif playerSex == sexList[1]:
            cache.featuresList['Age'] = featuresList["Age"][1]
        else:
            cache.featuresList['Age'] = featuresList["Age"][2]
        pycmd.clr_cmd()
        cache.temporaryObject['Features'] = cache.featuresList.copy()
        playerAgeTemName = attr.getAgeTemList()[1]
        playerAge = attr.getAge(playerAgeTemName)
        cache.temporaryObject['Age'] = playerAge
        detailedSetting_func2()
    pass

def detailedSetting_func2():
    eprint.p('\n')
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('11'))
    ansList = textload.loadCmdAdv("detailedSetting2")
    yrn = ans.optionstr(ans.detailedsetting2, 5,True)
    if yrn == ansList[len(ansList)-1]:
        pycmd.clr_cmd()
        detailedSetting_func3()
    else:
        pycmd.clr_cmd()
        attr.setAnimalCache(yrn)
        detailedSetting_func3()
    pass

def detailedSetting_func3():
    eprint.p('\n')
    eprint.pline()
    eprint.pl(textload.loadMessageAdv('12'))
    yrn = ans.optionint(ans.detailedsetting3,1)
    pass

def acknowledgmentAttribute_func():
    cache.playObject['object']['0'] = cache.temporaryObject.copy()
    playerSex = cache.playObject['object']['0']['Sex']
    playerAge = cache.playObject['object']['0']['Age']
    title1 = textload.loadStageWordText('1')
    playerName = cache.playObject['object']['0']['Name']
    eprint.p('\n')
    eprint.plt(title1)
    eprint.pl(playerName)
    eprint.p(textload.loadStageWordText('2'))
    eprint.p(playerSex)
    eprint.p('\n')
    eprint.p(textload.loadStageWordText('3'))
    eprint.p(playerAge)
    eprint.p('\n')
    eprint.p(textload.loadStageWordText('4'))
    featuresList = cache.playObject['object']['0']['Features']
    featuresListStr = attr.getFeaturesStr(featuresList)
    eprint.pl(featuresListStr)
    eprint.pline()
    pass