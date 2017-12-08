$(document).ready(function () {
    var jumboHeight = $('.jumbotron').outerHeight();

    function parallax() {
        var scrolled = $(window).scrollTop();
        $('.bg').css('height', (jumboHeight - scrolled) + 'px');
    }

    $(window).scroll(function (e) {
        parallax();
    });

    $(".dropdown-menu li a").click(function () {

        console.log("Clicked");
        console.log($("#teamSelect").text($(this).text()));
        $("#teamSelect").html('<span>' + $(this).text() + '</span>' + ' ' + '<span class="caret"></span>');
    });

    /* form validation plugin */
    $.fn.goValidate = function () {
        var $form = this,
            $inputs = $form.find('input:text');

        var validators = {
            name: {
                regex: /^[A-Za-z]{3,}$/
            },
            pass: {
                regex: /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/
            },
            email: {
                regex: /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/
            },
            phone: {
                regex: /^[2-9]\d{2}-\d{3}-\d{4}$/,
            }
        };
        var validate = function (klass, value) {
            var isValid = true,
                error = '';

            if (!value && /required/.test(klass)) {
                error = 'This field is required';
                isValid = false;
            } else {
                klass = klass.split(/\s/);
                $.each(klass, function (i, k) {
                    if (validators[k]) {
                        if (value && !validators[k].regex.test(value)) {
                            isValid = false;
                            error = validators[k].error;
                        }
                    }
                });
            }
            return {
                isValid: isValid,
                error: error
            }
        };
        var showError = function ($input) {
            var klass = $input.attr('class'),
                value = $input.val(),
                test = validate(klass, value);

            $input.removeClass('invalid');
            $('#form-error').addClass('hide');

            if (!test.isValid) {
                $input.addClass('invalid');

                if (typeof $input.data("shown") == "undefined" || $input.data("shown") == false) {
                    $input.popover('show');
                }

            }
            else {
                $input.popover('hide');
            }
        };

        $inputs.keyup(function () {
            showError($(this));
        });

        $inputs.on('shown.bs.popover', function () {
            $(this).data("shown", true);
        });

        $inputs.on('hidden.bs.popover', function () {
            $(this).data("shown", false);
        });

        $form.submit(function (e) {

            $inputs.each(function () { /* test each input */
                if ($(this).is('.required') || $(this).hasClass('invalid')) {
                    showError($(this));
                }
            });
            if ($form.find('input.invalid').length) { /* form is not valid */
                e.preventDefault();
                $('#form-error').toggleClass('hide');
            }
        });
        return this;
    };
    $('form').goValidate();
});



