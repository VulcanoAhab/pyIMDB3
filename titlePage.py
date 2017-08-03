import requests

class Title(requests.Session):
    """
    """

    _baseUrl="http://akas.imdb.com/title/{titleId}"

    def __init__(self):
        """
        """
        super().__init__()
        self.headers={
            "User-Agent":"pyIMDB",
            "Accept-Language":"en",
            "Connection":"keep-alive"
        }

    def fetchTitle(self, titleId):
        """
        """
        _url=self._baseUrl.format(titleId=titleId)
        response=self.get(_url)
        response.raise_for_status()
        return response.text

# ====== command line calls
def fetchTitleTest():
    """
    """
    parse=argparse.ArgumentParser()
    parse.add_argument("--title_id", "-ti")
    args=parse.parse_args()
    if not args.title_id:return
    title=Title()
    title.fetchTitle(args.title_id)

if __name__ == "__main__":
    import argparse
    fetchTitleTest()
