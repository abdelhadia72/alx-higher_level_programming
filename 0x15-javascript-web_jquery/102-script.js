$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();

    $.ajax({
      type: 'GET',
      url: `https://www.fourtonfish.com/hellosalut/?lang=${lang}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
