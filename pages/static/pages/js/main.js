$(document).ready(function () {

    // If teammate known, display entry field for teammate name
    $("#knowTeammate label").click(function () {
        console.log($(this).text());
        if ($(this).children().attr("id") == "option1") {
            $('#pickTeammate').css('display', 'block');
        } else {
            $('#pickTeammate').css('display', 'none');
        }
    });

    $(function () {


        // This function gets cookie with a given name
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        var csrftoken = getCookie('csrftoken');

        /*
        The functions below will create a header with csrftoken
        */

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        function sameOrigin(url) {
            // test that a given url is a same-origin URL
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                    // Send the token to same-origin, relative URLs only.
                    // Send the token only if the method warrants CSRF protection
                    // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

    });

    // form validation plugin
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
    $('#contactForm').goValidate();


    // Submit post on submit
    $('#addRegistrant').on('submit', function (event) {
        event.preventDefault();
        add_registrant();
    });


    // AJAX for posting from register.html
    function add_registrant() {
        $.ajax({
            url: "add_registrant/", // the endpoint
            type: "POST", // http method
            // data sent with the post request
            data: {
                first_name: $('#txtFirstName').val(),
                last_name: $('#txtLastName').val(),
                email: $('#txtEmail').val(),
                teammate: $('#pickTeammate').val()
            },

            // handle a successful response
            success: function (json) {
                console.log(json);
                $('#txtFirstName').val(''); // remove the value from the inputs
                $('#txtLastName').val('');
                $('#txtEmail').val('');
                $('#pickTeammate').val('');
                
                // Display registration success
                $('#registrationResult').html("<span class='text-success bg-success text-center'>You're registered! Now buy a ticket and get practicing!</span>");
                // Clear registration success note
                setTimeout(function () {
                    $('#registrationResult').empty()
                }, 6000)
            },

            // handle a non-successful response
            error: function (xhr, errmsg) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    "<a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    // Submit post on submit
    $('#checkPromo').on('submit', function (event) {
        event.preventDefault();
        check_promo();
    });


    // AJAX for posting from register.html
    function check_promo() {
        $.ajax({
            url: "check_promo/", // the endpoint
            type: "POST", // http method
            // data sent with the post request
            data: {
                promo_code: $('#promoCode').val()
            },

            // handle a successful response
            success: function (json) {
                var data = JSON.parse(json);
                console.log(data.numTeams);
                // Hide the promo code field
                $('#promoEnter').css('display', 'none'); // remove the value from the inputs
                // Display the Team registration form
                $('#registerTeams').removeClass('hidden');

                // Trying to log the number of teams
                for (i = 0; i < data.numTeams; i++) {
                    console.log(i)
                }
            },

            // handle a non-successful response
            error: function (xhr, errmsg) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    "<a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
});



