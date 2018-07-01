$(function () {

    console.log("It's working!");

    $('#intro-test').css('display', 'none');
    $('#go-further').css('display', 'none');
    $(document).ready(function () {
        $('#intro-test').fadeIn(1300);
    });
    setTimeout(function () {
        $('#go-further').fadeIn(1300)
    }, 2000);


    $('#go-further').click(function () {
        $(this).fadeOut(1300);
        $('#intro-test').fadeOut(1300);
        setTimeout(function () {
            $('#prepare').fadeIn(1300)
        }, 2000)
    })


});