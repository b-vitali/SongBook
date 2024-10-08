import os
import re

# Function to read the lyrics and Spotify link from an HTML song file
def read_song_data(song_path):
    with open(song_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        # Use regular expressions to extract lyrics between <div class="multiline-text"> tags
        lyrics_match = re.search(r'<div class="multiline-text">(.+?)<\/div>', html_content, re.DOTALL)
        spotify_match = re.search(r'https://open\.spotify\.com/embed/track/([\w\d]+)\??', html_content)

        song_lyrics = lyrics_match.group(1).strip() if lyrics_match else None
        spotify_link = spotify_match.group(0) if spotify_match else None

        return song_lyrics, spotify_link

# Function to generate the HTML content for a song
def generate_song_html(song_title, song_lyrics, spotify_link):
    song_html = f'''
        <section id="{song_title.replace(" ", "")}">
            <h2>{song_title}</h2>
            <div style="display: flex; justify-content: center;">
                <button onclick="adjustFontSize(this, -1)">A-</button>
                <button onclick="adjustFontSize(this, 1)">A+</button>
            </div>
    '''

    if spotify_link:
        song_html += f'''
            <div style="display: flex; justify-content: center;">
                <iframe style="border-radius: 12px;" 
                src="{spotify_link}" 
                width="90%" height="152px" frameBorder="0" allowfullscreen="" 
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
             </div>
        '''

    song_html += f'''
            <div class="multiline-text">
{song_lyrics}
            </div>
        </section>
    '''

    return song_html

# Function to generate the HTML content for an author's songs
def generate_author_songs_html(author_name, songs):
    author_html = f'<li><a href="#{author_name.replace(" ", "")}">{author_name}</a><ul class="song-list">'
    for song_title, song_lyrics in sorted(songs.items()):
        author_html += f'<li><a href="#{song_title.replace(" ", "")}">{song_title}</a></li>'
    author_html += '</ul></li>'
    return author_html

# Function to generate the HTML content for a language songbook
def generate_language_songbook(language_name, authors, songs_content):
    language_html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="css/songs.css"> <!-- CSS for this page (you can add many) -->
            <link rel="stylesheet" type="text/css" href="css/colors.css">
            <link rel="icon" href="SongBook_logo.png" type="image/x-icon">
            <title>{language_name} Songs</title>
            <script src="JS/songs.js"></script> <!-- JS with the "printSong" and "printAllSongs" functions-->
            <script src="JS/common.js"></script><!-- JS with fetchLastCommit -->
            <script>
                function fetchLastCommit() {{
                    // Function to fetch the last commit (implementation needed)
                }}

                function adjustFontSize(button, change) {{
                    const songSection = button.closest('section');
                    const textContainer = songSection.querySelector('.multiline-text');
                    const currentFontSize = window.getComputedStyle(textContainer, null).getPropertyValue('font-size');
                    const newFontSize = parseFloat(currentFontSize) + change;

                    textContainer.style.fontSize = newFontSize + 'px';
                }}
            </script>
        </head>
        <body>
            <header>
                <h1>{language_name} Songs</h1>
            </header>
            <div class="container">
                <div class="sidebar">
                    <h2>Authors</h2>
                    <ul class="author-list">
                        {authors}
                    </ul>
                </div>
                <div class="content">
                    {songs_content}
                </div>
            </div>
            <nav>
                <a href="index.html">Main menu</a>
                <a href="Create Song.html">Add song (Offline)</a>
                <a onClick="printSong()">Print to PDF (Broken)</a>
                <a onClick="printAllSongs()">Print ALL (Offline)</a>
            </nav>
            <footer>
                <p>&copy; Our SongBook</p>
                <span id="last-commit"></span>
            </footer>
        </body>
        </html>
    '''

    return language_html

# Define the root directory where your song folders are located
root_directory = "songs"

# Traverse the directory structure and generate songbooks
for language_folder in os.listdir(root_directory):
    language_path = os.path.join(root_directory, language_folder)

    if os.path.isdir(language_path):
        authors_html = ""
        songs_content = ""
        authors = []

        for author_folder in os.listdir(language_path):  # Collect authors
            author_path = os.path.join(language_path, author_folder)

            if os.path.isdir(author_path):
                songs = {}
                for song_file in os.listdir(author_path):  # Collect songs
                    if song_file.endswith(".html"):
                        song_path = os.path.join(author_path, song_file)
                        song_title = os.path.splitext(song_file)[0]  # Remove file extension
                        song_lyrics, spotify_link = read_song_data(song_path)  # Read song data

                        if song_lyrics:
                            songs[song_title] = (song_lyrics, spotify_link)

                author_name = author_folder.replace('_', ' ')  # Convert underscores to spaces
                authors.append((author_name, songs))

        # Sort authors alphabetically
        authors = sorted(authors, key=lambda x: x[0])

        for author_name, songs in authors:
            authors_html += generate_author_songs_html(author_name, songs)
            songs_content += "\n".join([generate_song_html(title, lyrics, spotify_link) for title, (lyrics, spotify_link) in sorted(songs.items())])

        language_songbook = generate_language_songbook(language_folder, authors_html, songs_content)

        # Save the generated HTML to a file
        output_filename = f"{language_folder.replace(' ', '')}_songbook.html"
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(language_songbook)
