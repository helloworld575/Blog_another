function password1_judge(password1) {
            var $pwd_bar_on = $(".password-judge");
            var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
            var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
            var enoughRegex = new RegExp("(?=.{6,}).*", "g");
            if (enoughRegex.test(password1) === false) {
                $pwd_bar_on.removeClass('pwd-mid');
                $pwd_bar_on.removeClass('pwd-weak');
                $pwd_bar_on.removeClass('pwd-max');
                $pwd_bar_on.addClass('pwd-fob');
                return false;
            }
            else if (strongRegex.test(password1)) {
                $pwd_bar_on.removeClass('pwd-mid');
                $pwd_bar_on.removeClass('pwd-weak');
                $pwd_bar_on.removeClass('pwd-fob');
                $pwd_bar_on.addClass('pwd-max');
            }
            else if (mediumRegex.test(password1)) {
                $pwd_bar_on.removeClass('pwd-fob');
                $pwd_bar_on.removeClass('pwd-weak');
                $pwd_bar_on.removeClass('pwd-max');
                $pwd_bar_on.addClass('pwd-mid');
            }
            else {
                $pwd_bar_on.removeClass('pwd-mid');
                $pwd_bar_on.removeClass('pwd-fob');
                $pwd_bar_on.removeClass('pwd-max');
                $pwd_bar_on.addClass('pwd-weak');
            }
            return true;
        }

        function password_same(password1, password2) {
            return password1===password2
        }