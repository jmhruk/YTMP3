from pytubefix import Playlist

p = Playlist("https://www.youtube.com/playlist?list=PL1SHXFX3wIB0kzjJJhKYPJf14YxczlFOg")
for video in p.videos:
    video.streams.first().download(filename=str(video.title + ".mp3"))