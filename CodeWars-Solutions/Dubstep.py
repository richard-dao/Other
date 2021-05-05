# Python
def song_decoder(song):
    song = song.split("WUB")
    OGSong = []
    for x in song:
        if x != '':
            OGSong += [x]
    return ' '.join(OGSong)
