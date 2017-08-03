from titlePage import Title
from titleMiner import Miner



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

    def loadPage(self):
        """
        """
        self._pageText=self._req.fetchTitle(self._id)
        self._drill.setPage(self._pageText)

    @property
    def pageTitle(self):
        """
        """
        if not "page_title" in self._data:
            self._data["page_title"]=self._drill.mineTitle()
        return self._data["page_title"]


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


if __name__ == "__main__":

    import argparse
    fromIDTest()
