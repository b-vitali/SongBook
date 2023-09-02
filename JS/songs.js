/* Simple function to print the current song to PDF */
function printSong() {
    // Hide unnecessary elements
    const elementsToHide = ['header', '.container > .sidebar', 'nav', 'footer'];
    elementsToHide.forEach(element => {
        document.querySelector(element).style.display = 'none';
    });

    // Print the song content
    window.print();

    // Restore the visibility of hidden elements
    elementsToHide.forEach(element => {
        document.querySelector(element).style.display = 'block';
    });
}


/* Complex function to print ALL the songs in a single (organized) PDF */
function printAllSongs() {
    // Hide unnecessary elements
    const elementsToHide = ['header', '.container > .sidebar', 'nav', 'footer'];
    elementsToHide.forEach(element => {
        document.querySelector(element).style.display = 'none';
    });

    // Create a new window and start building the content
    const printWindow = window.open('', '_blank');
    let combinedContent = '<html><head><style>.multiline-text { font-family: "Courier New", monospace; font-size: 0.5em; word-wrap: break-word; white-space: pre; padding-left: 0; }';
    combinedContent += '@page { @top-center { content: counter(page) "/" counter(pages); } }';
    combinedContent += '</style></head><body>';
    
    // Generate the index from the existing structure
    const authorListItems = document.querySelectorAll('.author-list > li');
    combinedContent += '<section><h2>Song Index</h2><ul>';
    authorListItems.forEach(authorItem => {
        const authorName = authorItem.querySelector('a').textContent;
        combinedContent += '<li>' + authorName + '<ul>';
        
        const songListItems = authorItem.querySelectorAll('.song-list li a');
        songListItems.forEach(songItem => {
            const songId = songItem.getAttribute('href').substring(1);
            combinedContent += '<li><a href="#' + songId + '">' + songId + '</a></li>';
        });

        combinedContent += '</ul></li>';
    });
    combinedContent += '</ul></section>';

    // Add page break after the index
    combinedContent += '<div style="page-break-after: always;"></div>';

    // Add page numbers and copy song content
    const songSections = document.querySelectorAll('.content > section');
    songSections.forEach((section, index) => {
        combinedContent += '<section id="' + section.id + '">' + section.innerHTML + '</section>';
        
        // Add a page break after each song (except for the last one)
        if (index < songSections.length - 1) {
            combinedContent += '<div style="page-break-after: always;"></div>';
        }
    });

    combinedContent += '</body></html>';
    
    // Write and print the combined content
    printWindow.document.write(combinedContent);
    printWindow.document.close();
    printWindow.print();

    // Close the print window after printing
    printWindow.close();

    // Restore the visibility of hidden elements
    elementsToHide.forEach(element => {
        document.querySelector(element).style.display = 'block';
    });
}
