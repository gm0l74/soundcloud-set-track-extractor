#---------------------------------
# Soundcloud
# tests.py
#
# @ start date          07 11 2022
# @ last update         07 11 2022
#---------------------------------

#---------------------------------
# Imports
#---------------------------------
import unittest
from soundcloud import soundcloud_playlist

#---------------------------------
# TestSoundcloud
#---------------------------------
class TestSoundcloud(unittest.TestCase):
    def test_soundcloud_playlist_1(self):
        urls = soundcloud_playlist('https://soundcloud.com/erasojajao/sets/orbital-mix-best-of-1')
        self.assertEqual(len(urls), 109)

    def test_soundcloud_playlist_2(self):
        urls = soundcloud_playlist('https://soundcloud.com/discover/sets/charts-top:pop:pt')
        self.assertEqual(len(urls), 50)

    def test_soundcloud_playlist_3(self):
        with self.assertRaises(ValueError) as ctx:
            soundcloud_playlist('https://www.youtube.com/watch?v=f2JuxM-snGc')
        
        self.assertTrue('Couldn\'t find the playlist info.' in str(ctx.exception))

#---------------------------------
# Execute
#---------------------------------
if __name__ == '__main__':
    unittest.main()

    