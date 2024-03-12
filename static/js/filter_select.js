document.getElementById('filterSelect').addEventListener('change', function() {
    var selectedOption = this.value;
    var rows = document.querySelectorAll('#dataTable tbody tr');
    rows.forEach(function(row) {
        var filterValue = row.getAttribute('data-filter');
        if (selectedOption === '' || selectedOption === filterValue) {
            row.style.display = 'table-row';
            // console.log(selectedOption+filterValue)
        } else {
            row.style.display = 'none';
            // console.log(selectedOption+filterValue)
        }
    });
});