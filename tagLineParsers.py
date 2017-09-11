import re

# == helpers
findTag=re.compile(r"\\bTaglines:\\b|\\bSee more »\\b", re.I)



def parseCoverTagLine(value):
    """
    """
    if not value:return None
    tags=findTag.findall(value)
    return tags
