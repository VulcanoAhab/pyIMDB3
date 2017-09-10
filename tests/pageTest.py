import sys,os
direname=os.path.dirname
absolPath=os.path.abspath
addPath=absolPath(direname(direname(absolPath(__file__))))
sys.path.append(addPath)

import unittest
from titlePageMiner import Miner

class TestPage(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self._fd=open("tests/futureTest.html","r")
        self._html=self._fd.read()
        self._miner=Miner()
        self._miner.setPage(self._html)

    def tearDown(self):
        """
        """
        self._fd.close()

    def test_pageTitle(self):
        """
        """
        self.assertEqual("Back to the Future (1985) - IMDb",
                         self._miner.minePageTitle())

    def test_titleBar(self):
        """
        """
        equalBase={
            'title': 'back to the future',
            'release_year': '1985',
            'duration': '1h 56min',
            'genres': ['adventure', 'comedy', 'sci-fi']}
        self.assertEqual(equalBase, self._miner.mineTitleBar())

    def test_poster(self):
        """
        """
        posterUrl="https://images-na.ssl-images-amazon.com/"\
                  "images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1Mj"\
                  "gtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@"\
                  "._V1_UX182_CR0,0,182,268_AL_.jpg"
        self.assertEqual(posterUrl, self._miner.minePoster())

    def test_mainCast(self):
        """
        """
        mainCastDict=[{
        'actorId': 'nm0000150', 'actorName': 'michael j. fox'},
        {'actorId': 'nm0000502', 'actorName': 'christopher lloyd'},
        {'actorId': 'nm0000670', 'actorName': 'lea thompson'},
        {'actorId': 'nm0000417', 'actorName': 'crispin glover'},
        {'actorId': 'nm0001855', 'actorName': 'thomas f. wilson'},
        {'actorId': 'nm0920148', 'actorName': 'claudia wells'},
        {'actorId': 'nm0566013', 'actorName': 'marc mcclure'},
        {'actorId': 'nm0818274', 'actorName': 'wendie jo sperber'},
        {'actorId': 'nm0225191', 'actorName': 'george dicenzo'},
        {'actorId': 'nm0564589', 'actorName': 'frances lee mccain'},
        {'actorId': 'nm0866055', 'actorName': 'james tolkan'},
        {'actorId': 'nm0169454', 'actorName': 'j.j. cohen'},
        {'actorId': 'nm0797150', 'actorName': 'casey siemaszko'},
        {'actorId': 'nm0000708', 'actorName': 'billy zane'},
        {'actorId': 'nm0914023', 'actorName': 'harry waters jr.'}]
        self.assertEqual(mainCastDict, self._miner.mineMainCast())

    def test_scores(self):
        """
        """
        _baseScores={
            'metascore': 86,
            'reviews_count': {
                'user': 863,
                'critic': 200},
            'popularity': 228}
        self.assertEqual(_baseScores, self._miner.mineScores())


# == command line
if __name__ == "__main__":
    unittest.main()
