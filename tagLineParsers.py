import re

# == helpers
findTag=re.compile(r"Taglines\:\n(.*)", re.I)



def parseCoverTagLine(value):
    """
    """
    if not value:return None
    tags=[t.strip() for t in findTag.findall(value) if t]
    if not len(tags):return None
    return tags[0]
