def make_album(artist, album_title, tracks=''):
    album = {'artist': artist.title(), 'title': album_title.title(),}
    if tracks:
        album['tracks'] = tracks
    return album

cg_album = make_album('childish gambino', 'kauai')
print(cg_album)
am_album = make_album('arctic monkeys', 'favourite worst nightmare')
print(am_album)
g_album = make_album('gorillaz', 'demon days')
print(g_album)
tp_album = make_album('twenty one pilots', 'vessel', 12)
print(tp_album)