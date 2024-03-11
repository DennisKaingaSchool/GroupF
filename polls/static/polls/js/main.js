Certainly! I've added comments to explain each section of the code for better clarity:

```javascript
(function ($) {
    "use strict";

    // Spinner
    function hideSpinner() {
        // Delayed hiding of the spinner element
        setTimeout(function () {
            $('#spinner').toggleClass('show', false);
        }, 1);
    }
    hideSpinner();

    // Initiate the wowjs
    new WOW().init();

    // Sticky Navbar
    $(window).scroll(function () {
        var $stickyTop = $('.sticky-top');
        // Add shadow and adjust top position when scrolling down
        if ($(this).scrollTop() > 300) {
            $stickyTop.addClass('shadow-sm').css('top', '0px');
        } else {
            // Remove shadow and adjust top position when scrolling up
            $stickyTop.removeClass('shadow-sm').css('top', '-100px');
        }
    });

    // Back to top button
    $(window).scroll(function () {
        var $backToTop = $('.back-to-top');
        // Show or hide back-to-top button based on scroll position
        if ($(this).scrollTop() > 300) {
            $backToTop.fadeIn('slow');
        } else {
            $backToTop.fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        // Smooth scroll to the top on button click
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });

    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });

    // Portfolio isotope and filter
    var $portfolioContainer = $('.portfolio-container');
    var portfolioIsotope = $portfolioContainer.isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function () {
        // Highlight the selected filter and apply filtering
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');
        portfolioIsotope.isotope({ filter: $(this).data('filter') });
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });

})(jQuery);
```

These comments should provide a clear understanding of each section and make the code more accessible to anyone reading it.