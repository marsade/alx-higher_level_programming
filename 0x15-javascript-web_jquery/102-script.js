$(document).ready(function () {
  const lang = $('input#language_code').val();
  $('input#btn_translate').click(function () {
    url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
