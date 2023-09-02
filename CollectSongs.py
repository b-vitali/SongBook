import os
import re

# Function to read the lyrics from an HTML song file
def read_song_lyrics(song_path):
    with open(song_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        # Use regular expressions to extract lyrics between <div class="multiline-text"> tags
        match = re.search(r'<div class="multiline-text">(.+?)<\/div>', html_content, re.DOTALL)
        if match:
            return match.group(1).strip()

    return None

# Function to generate the HTML content for a song
def generate_song_html(song_title, song_lyrics):
    return f'''
        <section id="{song_title.replace(" ", "")}">
            <h2>{song_title}</h2>
            <div class="multiline-text">
{song_lyrics}
            </div>
        </section>
    '''

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
                fetchLastCommit();
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
                <a onClick="printSong()">Print to PDF (Broken)</a>
                <a onClick="printAllSongs()">Print ALL to PDF</a>
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
                        song_lyrics = read_song_lyrics(song_path)

                        if song_lyrics:
                            songs[song_title] = song_lyrics

                author_name = author_folder.replace('_', ' ') # Convert underscores to spaces
                authors.append((author_name, songs))

        # Sort authors alphabetically
        authors = sorted(authors, key=lambda x: x[0])

        for author_name, songs in authors:
            authors_html += generate_author_songs_html(author_name, songs)
            songs_content += "\n".join([generate_song_html(title, lyrics) for title, lyrics in sorted(songs.items())])

        language_songbook = generate_language_songbook(language_folder, authors_html, songs_content)

        # Save the generated HTML to a file
        output_filename = f"{language_folder.replace(' ', '')}_songbook.html"
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(language_songbook)
