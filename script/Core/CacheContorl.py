import concurrent.futures

# 流程用变量组
flowContorl = {}

# 主页监听控制流程用变量组
wframeMouse = {}

# cmd存储
cmdMap = {}

# 角色对象数据缓存组
characterData = {}

# npc模板列表
npcTemData = []

# 输入记录（最大20）
inputCache = []

nowInitMapId = ''

# 回溯输入记录用定位
inputPosition = {}

instructFilter = {}

# 富文本记录输出样式临时缓存
outputTextStyle = ''

familyRegionList = []
boysRegionList = []
girlsRegionList = []
familyRegionIntList = []
boysRegionIntList = []
girlsRegionIntList = []

# 富文本回溯样式记录用定位
textStylePosition = {}

# 存储服装类型数据
clothingTypeData = {}

# 富文本样式记录
textStyleCache = []

# 富文本精确样式记录
textOneByOneRichCache = {}

lastCursor = [0]

# 图片id
imageId = 0

# cmd数据
cmdData = {}

# 游戏时间
gameTime = {}

# 时间增量
subGameTime = 0

# 面板状态
panelState = {}

# 存档页面最大数量
maxSavePage = 0

# 现在所处的流程
nowFlowId = ''
oldFlowId = ''
tooOldFlowId = ''

# 课时数据
courseData = {}

# 教师科目经验
teacherCourseExperience = {}

oldCharacterId = 0

# 各年龄段总人数
TotalNumberOfPeopleOfAllAges = {}

# 各年龄段总体脂率
TotalBodyFatByage = {}

# 各年龄段平均体脂率
AverageBodyFatByage = {}

# 各年龄段总身高
TotalHeightByage = {}

# 各年龄段平均身高
AverageHeightByage = {}

# 身材描述文本权重数据
statureDescritionPrioritionData = {}

textWait = 0

mapData = {}
sceneData = {}

nowMap = []

randomNpcList = []

occupationCharacterData = {}

placeData = {}

# 可穿戴道具类型数据
wearItemTypeData = {}

# 当前上课时间状态
courseTimeStatus = {}
