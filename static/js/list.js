
// Each element with an attr "data-action" will have a click listener which is
// redirecting to the specified URL.
$("[data-action]").click(function(e) {
    e.preventDefault();
    var $el = $(this);
    var action = $el.data("action");
    if (parseInt($el.parent().css("opacity"), 10) !== 1) {
        return;
    }
    document.location = action;
});

// Disable animated button by setting a class
function disableAnimatedButton($el) {
    $el.data({ status: false });
    $el.addClass("disabled");
}

// When we touch a button.
$("[data-animated-button]").on("touchend", function(e) {
    e.stopPropagation();

    var $el = $(this);
    var status = $el.data("status") || false;

    // We disable all buttons except the one we are touching.
    $("[data-animated-button]").each(function() {
        if (this !== $el.get(0)) {
            disableAnimatedButton($(this));
        }
    });

    if (status) {
        // Enabling is always the default behaviour when touching button.
        // So we only have to manage the disabling.
        disableAnimatedButton($el);
    } else {
        // We can animate, so we remove the "disabled" class and set the status.
        // The animation is CSS-based, so automatic.
        $el.removeClass("disabled");
        $el.data({ status: true });
    }
});

// When we touch the document, we disable all the buttons.
// Note the e.stopPropagation() in the "touchend" listener on buttons,
// to avoid runing the document listener when we are on a button.
$(document).on("touchend", function(e) {
    $("[data-animated-button]").data({ status: false });
});


      
