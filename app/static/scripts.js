$('#modal-confirm').click(function(event){
    // Perform the action after modal confirm button is clicked.

    $('#form-submit').click(); // submitting the form
    event.preventDefault();
});
