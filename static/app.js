$(function () {

    console.log("It's working!");

    $('.question-content').css('display', 'none');

    $(document).ready(function () {
        $('#intro-test').fadeIn(1300);
    });
    setTimeout(function () {
        $('#go-further').fadeIn(1300)
    }, 2000);


    $('#go-further').click(function () {
        $(this).fadeOut(1300);
        $('#intro-test').fadeOut(1400);
        setTimeout(function () {
            $('#prepare').fadeIn(1400)
        }, 2100);
        setTimeout(function () {
            $('#prepare').fadeOut(1400)
        },4100);
        setTimeout(function () {
            $('#main-test label:first-of-type').fadeIn(1400)
        },6000)
    });



    $('.answer-radio').each(function () {
        $(this).click(function () {
            $(this).parent().fadeOut(50);
            $(this).parent().next().fadeIn(3000);
        })
    })



});