$(document).ready(function() {

    $('.profile_photo_change').on('click', function(){
        $('#id_image').trigger('click').on('change', function(){
            $('#id_image').parents('form').trigger("submit");
        });
        return false;
    });

    $('#userEdit').on('click', function() {
        $('#editWindow').toggle()
    });
});
