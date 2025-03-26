// Get the currently selected value of the country dropdown
let countrySelected = $('#id_default_country').val();

// If no country is selected, set the dropdown text color to a light gray
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

// Add an event listener for changes to the country dropdown
$('#id_default_country').change(function() {
    // Get the new value of the selected country
    countrySelected = $(this).val();

    // If no country is selected, set the text color to light gray
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        // If a country is selected, set the text color to black
        $(this).css('color', '#000');
    }
});