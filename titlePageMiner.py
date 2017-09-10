from lxml import html
from personParsers import parsePersonId, parsePersonName
from titleBarParsers import (parseDuration, parseTitle,
                            parseReleaseYear, parseGenreList,
                            parsePosterLink)

from scoresParsers import parseReviewsCount

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
        if len(listEl):return listEl[0]
        print("[-] Could not find: {}".format(targetName))
        return None

    @staticmethod
    def _getEls(listEl, targetName):
        """
        """
        if len(listEl):return listEl
        print("[-] Could not find: {}".format(targetName))
        return None

    @staticmethod
    def _getElFromParent(parentObj, xpathStr, targetName):
        """
        """
        if  parentObj is None:
            print("[-] No parent found for: {}".format(targetName))
            return None
        return Miner._getEl(parentObj.xpath(xpathStr), targetName)

    @staticmethod
    def _getElsFromParent(parentObj, xpathStr, targetName):
        """
        """
        if  parentObj is None:
            print("[-] No parent found for: {}".format(targetName))
            return None
        return Miner._getEls(parentObj.xpath(xpathStr), targetName)

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
        titleBlockElContainer=self._obj.xpath("//div[@class='titleBar']")
        titleBlockEl=Miner._getEl(titleBlockElContainer, "titleBar")
        #title header - title and relase year
        titleContainer=titleBlockEl.xpath("./div[@class='title_wrapper']/"\
                                          "h1[@itemprop='name']/text()")
        titleText=Miner._getEl(titleContainer, "title text")
        relYContainer=titleBlockEl.xpath("./div[@class='title_wrapper']/"\
                                         "h1[@itemprop='name']/"\
                                         "span[@id='titleYear']/a/text()")
        releaseText=Miner._getEl(relYContainer, "release year text")
        #subtitle - generic infos
        subtitleElContainer=self._obj.xpath("//div[@class='subtext']")
        subtitleEl=Miner._getEl(subtitleElContainer, "subtext")
        durXpath="./time[@itemprop='duration']/text()"
        durationText=Miner._getElFromParent(subtitleEl,durXpath,"duration")
        genListXpath="./a/span[@itemprop='genre']/text()"
        genreListText=Miner._getElsFromParent(subtitleEl,genListXpath,"genres")
        #titlebar dict result
        titleBar["title"]=parseTitle(titleText)
        titleBar["release_year"]=parseReleaseYear(releaseText)
        titleBar["duration"]=parseDuration(durationText)
        titleBar["genres"]=parseGenreList(genreListText)
        return titleBar

    def minePoster(self):
        """
        """
        posterContainer=self._obj.xpath("//div[@class='poster']/a/img/@src")
        posterLink=Miner._getEl(posterContainer, "poster link")
        return parsePosterLink(posterLink)

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

    def mineScores(self):
        """
        """
        scoresDict={
            "metascore":"not_detected",
            "reviews_count":{
                "user":-1,
                "critic":-1
            },
            "popularity":-1,
        }
        #container
        scordeGet=self._obj.xpath("//div[@class='titleReviewBar ']")
        scoreContainer=Miner._getEl(scordeGet, "metaContainer")
        #xpath
        _meta="./div/a/div[@class='metacriticScore score_favorable"\
              " titleReviewBarSubItem']/span/text()"
        _userRev="./div/div/span/a[contains(text(), 'user')]/text()"
        _criticRev="./div/div/span/a[contains(text(), 'critic')]/text()"
        _popular="./div/div/div/span[contains(text(), '(')]/text()"
        #targetValues
        _metaRawGrade=Miner._getElFromParent(scoreContainer,
                                             _meta, "metascore")
        _userRevRawCount=Miner._getElFromParent(scoreContainer,
                                                _userRev, "users reviews")
        _criticRevRawCount=Miner._getElFromParent(scoreContainer,
                                                _criticRev, "critic reviews")
        _popularityRankRaw=Miner._getElFromParent(scoreContainer,
                                               _popular, "Popularity Rank")
        _userRevParsedCount=parseReviewsCount(_userRevRawCount, "user")
        _criticRevParsedCount=parseReviewsCount(_criticRevRawCount, "critic")
        #setting results
        if _metaRawGrade:
            scoresDict["metascore"]=int(_metaRawGrade.strip())
        if _userRevParsedCount:
            scoresDict["reviews_count"]["user"]=_userRevParsedCount
        if _criticRevParsedCount:
            scoresDict["reviews_count"]["critic"]=_criticRevParsedCount
        if _popularityRankRaw:
            scoresDict["popularity"]=parseReviewsCount(_popularityRankRaw,"(")
        return scoresDict
