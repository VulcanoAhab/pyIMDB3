from titlePage import Title
from titlePageMiner import Miner



class fromID():
    """
    """

    def __init__(self, titleId, **kwargs):
        """
        """
        #working classes
        self._req=Title()
        self._drill=Miner()
        #target title
        self._id=titleId
        #mined data container
        self._data={}

    def _testData(self, key, valueFunc):
        """
        """
        if key in self._data:return
        self._data[key]=valueFunc()

    def loadPage(self):
        """
        """
        self._pageText=self._req.fetchTitle(self._id)
        self._drill.setPage(self._pageText)

    @property
    def pageTitle(self):
        """
        """
        self._testData("page_title", self._drill.minePageTitle)
        return self._data["page_title"]

    @property
    def titleBar(self):
        """
        """
        self._testData("title_bar", self._drill.mineTitleBar)
        return self._data["title_bar"]

    @property
    def posterLink(self):
        """
        """
        self._testData("poster_link", self._drill.minePoster)
        return self._data["poster_link"]

    @property
    def mainCastList(self):
        """
        """
        self._testData("cast_list", self._drill.mineMainCast)
        return self._data["cast_list"]


# ===== command line
def fromIDTest():
    """
    """
    parse=argparse.ArgumentParser()
    parse.add_argument("--title_id", "-ti")
    args=parse.parse_args()
    if not args.title_id:return
    titlePross=fromID(args.title_id)
    titlePross.loadPage()
    print("[+] Page title: ",titlePross.pageTitle)
    print("[+] Cast list: ",titlePross.mainCastList)
    print("[+] Title barDict: ", titlePross.titleBar)
    print("[+] Poster link: ", titlePross.posterLink)


if __name__ == "__main__":

    import argparse
    fromIDTest()
