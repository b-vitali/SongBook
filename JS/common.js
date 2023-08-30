// Function to fetch the last commit date/time
async function fetchLastCommit() {
    const repoOwner = 'b-vitali';
    const repoName = 'SongBook';
    
    try {
        const response = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/commits`);
        const data = await response.json();
        
        if (data.length > 0) {
            const lastCommitDate = new Date(data[0].commit.committer.date);
            const formattedDate = lastCommitDate.toLocaleString();
            document.getElementById('last-commit').textContent = `Last Commit: ${formattedDate}`;
        }
    } catch (error) {
        console.error('Error fetching commit information:', error);
    }
}