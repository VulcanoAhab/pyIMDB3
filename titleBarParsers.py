def parseDuration(value):
    """
    """
    if not value: return None
    return value.strip()

def parseTitle(value):
    """
    """
    if not value: return None
    return value.strip().lower()

def parseReleaseYear(value):
    """
    """
    if not value: return None
    return value.strip()

def parseGenreList(value):
    """
    """
    if not isinstance(value, list) or not value:return []
    return [v.lower() for v in value]
