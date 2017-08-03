from lxml import html

class Miner():
    """
    """

    @staticmethod
    def _testEls(listEl, targetName):
        """
        """
        size=len(listEl)
        if not size:print("[-] Could not find: {}".format(targetName))
        return size

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
        titleContainer=self._obj.xpath(".//title/text()")
        if not Miner._testEls(titleContainer, "page title"):return
        return titleContainer[0]

    def mineActors(self):
        """
        """
        castElement=self._obj.xpath(".//table[@class='cast_list']")
        if not Miner._testEls(castElement,"cast table"):return
        castRows=castElement[0].xpath(".//tr[@class='even' or @class='odd']")
        if not Miner._testEls(castRows,"cast rows"):return
        for castRow in castRows:
            tdImage=castRow.xpath(".//td[@class='primary_image']")
