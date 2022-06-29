# prints info about one song
def print_list(a_list):
  for i in a_list:
    print(f"Artist: {i['artist']}")
    print(f"Song: {i['song_name']}")
    print(f"Genre: {i['genre']}")
    print(f"Year: {i['release_year']}")
    print("")

# given a list of dictionaries and an artist, returns the index of the dictionary within the list
def find_dictionary_by_artist(list, artist):
  index=0
  for i in list:
    if i["artist"]==artist:
      return index
    index+=1   


# the initial list
fav_songs=[
  {"artist":"Yes", "song_name":"Close to the Edge", "genre":"Prog rock", "release_year":"1972" },
  {"artist":"Beethoven", "song_name":"Ninth Symphony", "genre":"Choral Symphony", "release_year":"1824"},
  {"artist":"C418", "song_name":"Taswell", "genre":"Game", "release_year":"2013"},
]

# print header, with a couple of empty lines before and one after
print("\n\nList of favourite songs:\n")

#print the initial list
print_list(fav_songs)
print("") # empty line for readability

# add a new song and print list again
new_song={"artist":"Rush", "song_name":"2112", "genre":"Rock", "release_year":"1976"}
fav_songs.append(new_song)
print_list(fav_songs)
print("")

# add another new song and print list
new_song={"artist":"Hawkwind", "song_name":"Psychedelic Warlords", "genre":"Space Rock", "release_year":"1974"}
fav_songs.append(new_song)
print_list(fav_songs)
print("")

# remove C418:Taswell song and print list
fav_songs.pop(2)
print_list(fav_songs)
print("")

#change the year on one song by named artist. This will of course break if the artist has two songs, in which case we need to search for the song name as well
index=find_dictionary_by_artist(fav_songs,"Rush")
#print(index) works, = 2
#fav_songs[index]["release_year"]="1975"   # works 
fav_songs[index].update({"release_year":"1975"})  # also works


# and print the new list
print_list(fav_songs)
print("")





