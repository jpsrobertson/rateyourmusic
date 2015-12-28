import os, urllib, imghdr

def create_if_needed(directory):

    if not os.path.isdir(directory):
        os.makedirs(directory)


class AlbumEntry:

    def __init__(self):

        self.primary_issue  = None
        self.genres         = set()

    def retrieve_cover_art(self, cover_art):

        folder = 'cover_art'
        create_if_needed(folder)

        tmp_file = folder + '/' + self.title.replace(' ', '_')
        urllib.request.urlretrieve(cover_art, tmp_file)

        image_ext = imghdr.what(tmp_file)

        self.cover_art_file = os.path.abspath(tmp_file + "." + image_ext)
        os.rename(tmp_file, self.cover_art_file)
    
    def print_info(self):
        
        print("Album title:\t%s" % self.title)
        print("Artist:\t\t%s" % self.artist)
        print("Release date:\t%s-%s-%s\n" % (self.year, self.month, self.day))
        
        print("Tracklist:")
        print(self.full_tracklist)

        if len(self.genres) > 0:
            print("Genres:")
            
            for g in self.genres:
                print(g)
