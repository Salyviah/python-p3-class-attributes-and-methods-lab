class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        Song.add_song_to_count()

        # Add artist and genre
        self.add_to_artists()
        self.add_to_genres()

        # Add to genre and artist count
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        # Add genre if it's not already in the list
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        # Add artist if it's not already in the list
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        # Increment the genre count or set it to 1 if it's a new genre
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        # Increment the artist count or set it to 1 if it's a new artist
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

# Example usage
song1 = Song("up", "Cardi", "Rap")
song2 = Song("shape of you", "", "Rnb")
song3 = Song("I like", "Rubi Rose", "Rap")

print(Song.count)  # => 3
print(Song.artists)  # => ['Jay-Z', 'Cardi B', 'Drake']
print(Song.genres)  # => ['Rap', 'Pop']
print(Song.genre_count)  # => {'Rap': 2, 'Pop': 1}
print(Song.artist_count)  # => {'Jay-Z': 1, Cardi B': 1, 'Drake': 1}

