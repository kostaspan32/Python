from video import Video
from random import randrange


class Playlist:
    def __init__(self, title, description, videos):
        self.title = title
        self.description = description
        self.videos = videos
        self.total_duration = sum([video.duration for video in videos])

    def add_video(self, other):
        if isinstance(other, Video):
            self.videos += other

    def __str__(self):
        playlist_songs = [str(video) for video in self.videos]
        return f'{"="*20}\nPlaylist title: {self.title}\nDescription: {self.description}\nVideos: {",".join(playlist_songs)}\n{"="*20}'

    def recommendation(self):
        x = randrange(len(self.videos))
        return f'My recommendation is {self.videos[x]}'

v1 = Video('Led Zeppelin', 'Stairway to Heaven', 7)
v2 = Video('Trannos', 'COCO', 3)
v3 = Video('Queen', 'Bohemian Rhapsody', 8)
v_list = [v1, v2, v3]

mine = Playlist('Party', 'Having Fun', v_list)
print(mine)




