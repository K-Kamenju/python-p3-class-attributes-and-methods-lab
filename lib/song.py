class Song:
    
    song_list = []
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}
    count = 0 
    
    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_song_to_list(name)
        self.add_artist_to_list(artist)
        self.add_genres_to_list(genre)
        self.add_artist_count(artist)
        self.add_genre_count(genre)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    @classmethod
    def add_song_to_list(cls, name):
        cls.song_list.append(name)
        
    @classmethod
    def print_song_list(cls):
        print([song for song in cls.song_list])
        
    @classmethod
    def add_artist_to_list(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
            
    @classmethod
    def add_genres_to_list(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    

test_case_1 =  Song("99 Problems", "Jay Z", "Rap")
test_case_2 =  Song("Halo", "Beyonce", "Pop")
test_case_3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)
