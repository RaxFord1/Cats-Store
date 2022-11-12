$("#login_section").hide();
$("#register_section").hide();

$("#navbar_login_button").on( "click", function( event ) {
    $("#register_section").hide();
    $("#login_section").show();
});

$("#navbar_register_button").on( "click", function( event ) {
    $("#login_section").hide();
    $("#register_section").show();
});
