/**
 * Created by orkan on 18.12.15.
 */

(function(){
    $(document).ready(function(){


        var res = $('#registration_form').validate({
            rules:{
                first_name: "required",
                last_name: "required",
                username: {
                    required: true,
                    minlength: 3
                },
                password: {
                    required: true,
                    minlength: 2
                },
                confirm_password: {
                    required: true,
                    minlength: 2,
                    equalTo: "#password"
                }

            }
        });


        $('#registration_form').submit(function(){

            if (res.valid()) {

                var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

                //var f_data = {};
                //var arr = $('#registration_form').serializeArray();
                //for (var i=0; i<arr.length; i++) {
                //    f_data[arr[i].name] = arr[i].value;
                //}

                $.ajax({
                    url: url_cup_organizer_create,
                    type: "POST",
                    data: $('#registration_form').serialize(),
                    dataType: 'json',
                    contentType: 'application/json',
                    beforeSend: function(xhr, settings) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                    success: function (data) {
                        console.log('Organizer create response: ' + JSON.stringify(data));
                    },
                    error: function () {
                        console.log('ERROR: something wrong');
                    }
                });
            } else {
                console.log('registration organizer invalid');
            }
            return false;
        });

    });
})();