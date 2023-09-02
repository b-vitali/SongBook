# SongBook
## How to use it
Hi, this is my SongBook!
The idea is quite simple:
- Add songs (as `html` files) or authors (as `folders`) 
- Run the `CollectSongs.py`
- Emjoy the Songbook!

## Structure
The layout of the repo is the following:

### Main part
- index.html
- CollectSongs.py
- songs
    - language1
        - author1
            - song1
            - song2
            - ...
        - author2
            - ...
    - language2
        - ...
    - ...

Running CollectSongs.py will generate language1_songbook.html, language2_songbook.html, ...

Changes in the folders for the authors and/or in the html files for the songs will be 

automatically propagated to these _songbook.html.

NB: now these are **not** collected automatically in the index. 

**If you add a language you need to link it manually, following the example**

### Estetics
- png for the logo
- LogoColor.py to change it
- CSS
    - colors.css for the palette
    - index.css  for formatting
    - songss.css for formatting

### Additional functionality
- JS
    - common.js to fetch the last commit
    - songs.js  to print to file the lyrics 

