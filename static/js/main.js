$("#login_section").hide();
$("#register_section").hide();
$(".form-conteiner").hide();
$(".form-close-bg").hide();
$(".exit-reg-bg").hide();
$(".exit-login-bg").hide();

$(".exit-reg-bg").on( "click", function( event ) {
    $("#register_section").hide();
    $(".exit-reg-bg").hide();
});

$(".exit-login-bg").on( "click", function( event ) {
    $("#login_section").hide();
    $(".exit-login-bg").hide();
});

$(".reg-close-icon").on( "click", function( event ) {
    $("#register_section").hide();
    $(".exit-reg-bg").hide();
});
$(".log-close-icon").on( "click", function( event ) {
    $("#login_section").hide();
    $(".exit-login-bg").hide();
});
$("#navbar_register_button").on( "click", function( event ) {
    $(".exit-login-bg").hide();
    $("#login_section").hide();
    $("#register_section").show();
    $(".exit-reg-bg").show();
});

$("#navbar_login_button").on( "click", function( event ) {
    $(".exit-reg-bg").hide();
    $("#register_section").hide();
    $("#login_section").show();
    $(".exit-login-bg").show();
});

$("body").on("click", ".btn-form-photo", function(){
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
