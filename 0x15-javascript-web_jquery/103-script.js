$(document).ready(function () {
  // Function to fetch and print the translation of "Hello"
  function fetchAndPrintTranslation () {
    // Get the language code from the input field
    const lang = $('#language_code').val();
    url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    })
      .fail(function (error) {
        console.error('Error fetching translation:', error);
      });
  }

  $('#btn_translate').click(fetchAndPrintTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchAndPrintTranslation();
    }
  });
});
