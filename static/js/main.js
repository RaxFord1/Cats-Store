
$("#login_section").hide();
$("#register_section").hide();
$(".form-conteiner").hide();
$(".form-close-bg").hide();

$("#navbar_login_button").on( "click", function( event ) {
    $("#register_section").hide();
    $("#login_section").show();
});
$("#navbar_register_button").on( "click", function( event ) {
    $("#login_section").hide();
    $("#register_section").show();
});
$(".btn-form-photo").on( "click", function( event ) {
    $(".form-conteiner").show();
    $(".form-close-bg").show();
});
$(".exit-icon").on( "click", function( event ) {
    $(".form-conteiner").hide();
    $(".form-close-bg").hide();
});

$(".btn-exit").on( "click", function( event ) {
    $(".form-conteiner").hide();
    $(".form-close-bg").hide();
});
$(".form-close-bg").on( "click", function( event ) {
    $(".form-conteiner").hide();
    $(".form-close-bg").hide();
});
