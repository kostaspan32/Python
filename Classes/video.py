class Video:
    def __init__(self, artist_name, song_name, duration):
        self.artist_name = artist_name
        self.song_name = song_name
        self.duration = duration

    def __str__(self):
        return f'{self.artist_name} - {self.song_name}'

v1 = Video('Led Zeppelin', 'Stairway to Heaven', 7)
v2 = Video('Trannos', 'COCO', 3)
v3 = Video('Queen', 'Bohemian Rhapsody', 8)
v_list = [v1, v2, v3]
