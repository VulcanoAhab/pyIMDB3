def parseReviewsCount(textIn, replaceStr):
    """
    """
    if not textIn:return None
    _text=textIn.replace(replaceStr, "")
    return int(_text.strip())
