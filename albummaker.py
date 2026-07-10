#create record albums with optional track numbers

def create_album(artist_name, album_title, track_number=None):
    """Create a dictionary representing an album."""
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    if track_number:
        album['tracks'] = track_number
    return album

def print_album(album):
    """Print the album information."""
    print(f"Artist: {album['artist']}")
    print(f"Album: {album['album']}")
    if 'tracks' in album:
        print(f"Tracks: {album['tracks']}")

album_library = []
def add_album_to_library(created_album):
    """Add the created album to the album library."""
    album_library.append(created_album)

def request_album_info():
    """Request album information from the user."""
    artist_name = input("Enter the artist's name: ")
    album_title = input("Enter the album title: ")
    track_number_input = input("Enter the number of tracks (optional): ")
    
    # Convert track number to an integer if provided
    track_number = int(track_number_input) if track_number_input else None
    add_album_to_library(create_album(artist_name, album_title, track_number))
    
created_album = create_album('Pink Floyd', 'The Dark Side of the Moon', 10)
another_album = create_album('The Beatles', 'Abbey Road')
other_album = create_album('Led Zeppelin', 'IV')

print_album(created_album)
add_album_to_library(created_album)
add_album_to_library(another_album)
add_album_to_library(other_album)
request_album_info()
request_album_info()


print("\nAlbum Library:")
for album in album_library:
    print_album(album)
    print()  # Print a blank line between albums
