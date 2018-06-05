import time
import core.GameConfig as config
import core.TextHandle as text
import core.flow as flow
import core.pyio as pyio
import core.CacheContorl as cache
import core.Dictionaries as doctionaries
import core.RichText as richtext
import core.TextLoading as textload

last_char = '\n'

#默认输出样式
def_style = pyio.style_def

#基本输出
def p(string, style='standard'):
    barlist = textload.getTextData(textload.barListId,'barlist')
    styleList = richtext.setRichTextPrint(string, style)
    global last_char
    if len(string) > 0:
        last_char = string[-1:]
    string = richtext.removeRichCache(string)
    for i in range(0,len(string)):
        if styleList[i] in barlist:
            styledata = textload.getTextData(textload.barListId,styleList[i])
            truebar = styledata['truebar']
            nullbar = styledata['nullbar']
            if string[i] == '0':
                pimage(nullbar, 'bar')
            elif string[i] == '1':
                pimage(truebar, 'bar')
            else:
                pyio.print(string[i], styleList[i])
        else:
            pyio.print(string[i], styleList[i])

# 输出图片
def pimage(imageName,imagePath=''):
    pyio.imageprint(imageName,imagePath)
    pass

# 小标题输出
def plt(string):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    string = str(string)
    string = doctionaries.handleText(string)
    global last_char
    if len(string) > 0:
        last_char = string[-1:]
    width = config.text_width
    textWidth = text.getTextIndex(string)
    lineWidth = int(int(width)/2 - int(textWidth)/2 - 2)
    pl('='*lineWidth + '<littletitle>▢' + string + '▢</littletitle>' + '='*lineWidth)

# 子标题输出
def sontitleprint(string):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    string = string
    string = doctionaries.handleText(string)
    global last_char
    if len(string) > 0:
        last_char = string[-1:]
    width = config.text_width
    textWidth = text.getTextIndex(string)
    lineWidth = int(int(width)/4)
    lineWidthFix = int(int(width)/4 - int(textWidth))
    pl(':' * lineWidthFix + '<sontitle>' + string + '</sontitle>' + ':' * lineWidth * 3)

#输出一行
def pl(string='', style='standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    global last_char
    if not last_char == '\n':
        p('\n')
    p(str(string), style)
    if not last_char == '\n':
        p('\n')

#输出分割线
def pline(sample='=', style='standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    textWidth = config.text_width
    pl(sample * textWidth,style)

def plittleline(sample = ':',style = 'standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    textWidth = config.text_width
    pl(sample * textWidth, style)

# 输出页数线
def printPageLine(sample = ':',string = '',style = 'standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    textWidth = int(config.text_width)
    stringWidth = int(text.getTextIndex(string))
    fixText = sample * int(textWidth / 2 - stringWidth / 2)
    stringText = fixText + string + fixText
    p(stringText,style)

#输出警告
def pwarn(string, style='warning'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    """输出警告"""
    pl(string, style)
    print(string)

#输出并等待
def pwait(string, style='standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    p(string, style)
    flow.askfor_wait()

#输出一行并等待
def plwait(string='', style='standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    pl(string, style)
    flow.askfor_wait()

#逐字输出
def pobo(sleepTime,string, style='standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    cache.wframeMouse['wFrameUp'] = 0
    styleList = richtext.setRichTextPrint(string,style)
    styleNameList = config.getFontDataList()
    for i in range(0,len(styleNameList)):
        styleTextHead = '<' + styleNameList[i] + '>'
        styleTextTail = '</' + styleNameList[i] + '>'
        if styleTextHead in string:
            string = string.replace(styleTextHead,'')
            string = string.replace(styleTextTail, '')
        else:
            pass
    index = len(string)
    for i in range(0,index):
        p(string[i],styleList[i])
        time.sleep(sleepTime)
        if cache.wframeMouse['wFrameUp'] == 1:
            indexI = i + 1
            cache.wframeMouse['wFrameUp'] = 2
            for indexI in range(indexI,index):
                p(string[indexI],styleList[indexI])
            if cache.wframeMouse['wFrameLineState'] == 2:
                cache.wframeMouse['wFrameLinesUp'] = 2
            break

# 列表输出
def plist(stringList,stringColumn = 1,stringSize = 'left'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    textWidth = config.text_width
    stringIndex = int(textWidth / stringColumn)
    for i in range(0, len(stringList)):
        stringText = stringList[i]
        stringIdIndex = text.getTextIndex(stringList[i])
        if stringSize == 'left':
            stringTextFix = ' ' * (stringIndex - stringIdIndex)
            stringText = stringText + stringTextFix
        elif stringSize == 'center':
            stringTextFix = ' ' * int((stringIndex - stringIdIndex) / 2)
            stringText = stringTextFix + stringText + stringTextFix
        elif stringSize == 'right':
            stringTextFix = ' ' * (stringIndex - stringIdIndex)
            stringText = stringTextFix + stringText
        if i == 0:
            p(stringText)
        elif i / stringColumn >= 1 and i % stringColumn == 0:
            p('\n')
            p(stringText)
        else:
            p(stringText)

#切换下一屏
def pnextscreen():
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    p('\n' * config.text_hight)

#多行居中逐字输出
def lcp(sleepTime,string='',style='standard'):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    cache.wframeMouse['wFrameLineState'] = 1
    string = str(string)
    stringlist = string.split('\n')
    width = config.text_width
    styleNameList = config.getFontDataList()
    stringCenterList = ''
    for i in range(0, len(styleNameList)):
        styleTextHead = '<' + styleNameList[i] + '>'
        styleTextTail = '</' + styleNameList[i] + '>'
        if styleTextHead in string:
            stringCenter = string.replace(styleTextHead, '')
            stringCenter = stringCenter.replace(styleTextTail, '')
            stringCenterList = stringCenter.split('\n')
        else:
            stringCenterList = stringlist
    for i in range(0,len(stringlist)):
        widthI = int(width) / 2
        countIndex = text.getTextIndex(stringCenterList[i])
        countI = int(countIndex) / 2
        if cache.wframeMouse['wFrameRePrint'] == 1:
            p('\n')
            p(' ' * int((widthI - countI)))
            p(stringlist[i])
        else:
            p(' ' * int((widthI - countI)))
            pobo(sleepTime, stringlist[i])
            p('\n')
            if cache.wframeMouse['wFrameLinesUp'] == 1:
                indexIUp = i + 1
                cache.wframeMouse['wFrameLinesUp'] = 2
                for indexIUp in range(indexIUp, len(stringlist)):
                    pl(text.align(stringlist[indexIUp], 'center'), style)
                cache.wframeMouse['wFrameLineState'] = 2
                break
    cache.wframeMouse['wFrameRePrint'] = 0

#多行回车逐行输出
def lkeyp(string=''):
    textWait = cache.textWait
    if textWait != 0:
        time.sleep(textWait)
    else:
        pass
    cache.wframeMouse['wFrameMouseNextLine'] = 1
    string = str(string)
    stringlist = string.split('\n')
    for i in range(0,len(stringlist)):
        plwait(stringlist[i])
    cache.wframeMouse['wFrameMouseNextLine'] = 0