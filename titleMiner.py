from lxml import html
from personParsers import parsePersonId, parsePersonName

class Miner():
    """
    """

    @staticmethod
    def _existsEl(listEls, targetName):
        """
        """
        size=len(listEls)
        if not size:print("[-] Could not find: {}".format(targetName))
        return size

    @staticmethod
    def _getEl(listEl, targetName):
        """
        """
        if listEl:return listEl[0]
        print("[-] Could not find: {}".format(targetName))
        return None


    def __init__(self, engine=html):
        """
        """
        self._engine=engine

    def setPage(self, pageText):
        """
        """
        self._rawPage=pageText
        self._obj=self._engine.fromstring(self._rawPage)

    def minePageTitle(self):
        """
        """
        titleContainer=self._obj.xpath("//title/text()")
        return Miner._getEl(titleContainer, "page title")

    def mineTitleBar(self):
        """
        """
        titleBar={}
        titleBlockEl=self._obj.xpath("//div[@class='titleBar']")
        titleContainer=self._obj.xpath("./div[@class='title_wrapper']/"\
                                          "h1[@itemprop='name']/text()")
        #title header - title and relase year
        titleText=Miner._getEl(titleContainer, "title text")
        releaseYearContainer=self._obj.xpath("./div[@class='title_wrapper']/"\
                                             "h1[@itemprop='name']/"\
                                             "span[@id='titleYear']/a/text()")
        releaseText=Miner._getEl(releaseYearContainer, "release year text")
        #subtitle - generic infos
        subtitle=self._obj.xpath("./div[@class='subtext']")


        titleBar["title"]=titleText
        titleBar["release_year"]=releaseText


    def mineMainCast(self):
        """
        """
        castElement=self._obj.xpath("//table[@class='cast_list']")
        if not Miner._existsEl(castElement,"cast table"):return
        castRows=castElement[0].xpath("./tr[@class='even' or @class='odd']")
        if not Miner._existsEl(castRows,"cast rows"):return
        castList=[]
        for castRow in castRows:
            tdPersonEl=castRow.xpath("./td[@itemprop='actor']")
            tdPersonProp=Miner._getEl(tdPersonEl, "actor_element")
            castPersonIdEl=tdPersonProp.xpath("./a/@href")
            castPersonId=Miner._getEl(castPersonIdEl, "actor_id")
            castPersonNameEl=tdPersonProp.xpath("./a/span/text()")
            castPersonName=Miner._getEl(castPersonNameEl, "actor_name")
            castList.append({
                "actorId":parsePersonId(castPersonId),
                "actorName":parsePersonName(castPersonName)
            })
        return castList
