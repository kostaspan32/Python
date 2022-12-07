from video import Video
from playlist import Playlist


class ClassicalPlaylist(Playlist):
    def __init__(self, title, description, videos, era):
        super().__init__(title, description, videos)
        self.era = era

    def __str__(self):
        playlist_songs = ",".join([str(video) for video in self.videos])
        return f'{"=" * 20}\nPlaylist title: {self.title}\nDescription: {self.description}' \
               f'\nVideos:{playlist_songs}\nEra: {self.era}\n{"=" * 20}'

    def recommendation(self):
        return f'My recommendation is {self.videos[0]}'


v1 = Video('Led Zeppelin', 'Stairway to Heaven', 7)
v2 = Video('Trannos', 'COCO', 3)
v3 = Video('Queen', 'Bohemian Rhapsody', 8)
v_list = [v1, v2, v3]

mine = Playlist('Party', 'Having Fun', v_list)
yours = ClassicalPlaylist('Study', 'Educational music', v_list, 'Baroque')
print(mine)
print(yours)
print(mine.recommendation())
print(yours.recommendation())

