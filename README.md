# SongBook
## How to use it
Hi, this is my SongBook!
The idea is quite simple:
- Add songs (as `html` files) or authors (as `folders`) 
- Run the `CollectSongs.py`
- Emjoy the Songbook!

It can be used offline, opening `index.html` in a web browser

OR via a GitHub Page, based on a GitHub Repository.

This is the case for the [page](https://b-vitali.github.io/SongBook/) based on this repo.
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

Running CollectSongs.py will generate `language1_songbook.html`, `language2_songbook.html`, ...

Changes in the folders for the authors and/or in the html files for the songs will be 

automatically propagated to these "_songbook.html".

NB: As of right now, these are **not** collected automatically in the `index.html`. 

**If you add a language you need to link it manually, following the example**

### Esthetics
- PNG for the logo
- `LogoColor.py` to change it
- CSS
    - `colors.css` for the palette
    - `index.css`  for formatting
    - `songss.css` for formatting

### Additional functionality
- JS
    - `common.js` to fetch the last commit
    - `songs.js`  to print to file the lyrics 

