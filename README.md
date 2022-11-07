# SoundCloud Playlist/Set Tracks Extractor

## About

Since, as of November 2022, SoundCloud is no longer processing new
API application requests, and, thus, no longer providing API keys
to be used to obtain info on tracks and sets, this repository
issues a python3 function to extract streamable tracks from
SoundCloud playlists (aka sets).

To circumvent the lack of new API keys, we simply query
SoundCloud's web service with the playlist URL.
We, then, parse the HTTP response and extract each track's
unique identifier (id) from one of the HTML <script> tags.
Finally, in order to obtain a streamable URL for each track,
we use a Soundcloud embed link with the track id.

To know more about Embed links, see:
https://help.soundcloud.com/hc/en-us/articles/115003568008-Embedding-a-track-or-playlist-

Concluding, the function `soundcloud_playlist` (in soundcloud.py) is
responsible for taking in a playlist URL and returning a list
of streamable track URLs.

## Tests

To run the tests, simply run the following command:

```bash
$ python3 tests.py
```