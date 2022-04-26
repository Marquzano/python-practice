def make_album(artist, album_title, tracks=''):
    album = {'artist': artist.title(), 'title': album_title.title(),}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease tell us your favorite albums:")
    print("(Enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break
    
    album_name = input("Album name: ")
    if album_name == 'q':
        break

    tracks = int(input("Number of tracks (optional): "))
    if tracks == 'q':
        break

    album = make_album(artist, album_name, tracks)
    print(album)