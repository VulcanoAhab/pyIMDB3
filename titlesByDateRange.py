class MovieList:
    """
    dateFormat
    ----------
    YYYY-mm-dd
    """
    baseUrl="http://www.imdb.com/search/title?\
            release_date={start},{end}\
            &title_type=feature"
    pass


class TvMovieList:
    """
    dateFormat
    ----------
    YYYY-mm-dd
    """
    baseUrl="http://www.imdb.com/search/title?\
            release_date={start},{end}\
            &title_type=tv_movie"
    pass
