$(function() {

    var header = $('#header'),
        introH = $('#intro').innerHeight(),
        scrollOffset = $(window).scrollTop();

    checkScroll(scrollOffset);

    /* Fixed header */

    $(window).on("scroll", function() {
        scrollOffset = $(this).scrollTop();
        checkScroll(scrollOffset)

    });

    function checkScroll(scrollOffset) {

        if (scrollOffset >= introH) {
            header.addClass("fixed");
        } else {
            header.removeClass("fixed");
        }
    }

    /* Smooth scroll */

    $('[data-scroll]').on("click", function(event) {
        event.preventDefault();

        var blockID = $(this).data('scroll'),
            blockOffset = $(blockID).offset().top;

        $("html, body").animate({
            scrollTop: blockOffset
        }, Math.abs(blockOffset - scrollOffset) > 3000 ? 800 : 500);
    });

    /* Menu nav toggle */

    $("#nav-toggle").on("click", function(event) {
        event.preventDefault();

        $(this).toggleClass("active");
        header.toggleClass("active");
    })

});