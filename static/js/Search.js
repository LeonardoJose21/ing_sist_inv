document.getElementById('searchInput').addEventListener('input', function() {
    // Get the search input value
    var searchText = this.value.toLowerCase();
    
    // Get all table rows
    var rows = document.querySelectorAll('#dataTable tbody tr');
    
    // Loop through each table row
    rows.forEach(function(row) {
        // Get the text content of each cell in the row
        var cellText = row.textContent.toLowerCase();
        
        // Check if the row contains the search text
        if (cellText.includes(searchText)) {
            // Show the row if it contains the search text
            row.style.display = '';
        } else {
            // Hide the row if it does not contain the search text
            row.style.display = 'none';
        }
    });
});