import re

# == helpers
findId=re.compile(r"tt\d+", re.I)



def parseMovieId(value):
    """
    """
    idContainer=findId.findall(value)
    if not idContainer:return None
    return idContainer[0]
