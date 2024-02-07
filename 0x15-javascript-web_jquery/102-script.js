$(document).ready(function () {
    $('INPUT#btn_translate').click(function () { 
        const lang = $('INPUT#language_code').val();
        
        $.ajax({
            type: "GET",
            url: `https://mp01a3ec8ad59f5f472f.free.beeceptor.com/${lang}`,
            success: function (data) {
                $('DIV#hello').text(data.hello);
            }
        });
    });
});