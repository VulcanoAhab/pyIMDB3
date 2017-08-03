import re

# == helpers
findId=re.compile(r"nm\d+", re.I)



def parsePersonId(value):
    """
    """
    idContainer=findId.findall(value)
    if not idContainer:return None
    return idContainer[0]

def parsePersonName(value):
    """
    """
    if not value:return None
    return value.lower()
