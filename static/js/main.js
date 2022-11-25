$("#login_section").hide();
$("#register_section").hide();
$(".form-conteiner").hide();
$(".form-close-bg").hide();
$(".exit-reg-bg").hide();
$(".exit-login-bg").hide();

function closeAll() {
    $("#register_section").hide();
    $(".exit-reg-bg").hide();
    $("#login_section").hide();
    $(".exit-login-bg").hide();
    $(".form-conteiner").hide();
    $(".form-close-bg").hide();
    $(".form-select-cat-container").hide();
}

$(".exit-reg-bg").on( "click", function( event ) {
    closeAll()
});

$(".exit-login-bg").on( "click", function( event ) {
    closeAll()
});

$(".reg-close-icon").on( "click", function( event ) {
    closeAll()
});
$(".log-close-icon").on( "click", function( event ) {
    closeAll()
});
$("#navbar_register_button").on( "click", function( event ) {
    closeAll()
    $("#register_section").show();
    $(".exit-reg-bg").show();
});

$("#navbar_login_button").on( "click", function( event ) {
    closeAll()
    $("#login_section").show();
    $(".exit-login-bg").show();
});

$("body").on("click", ".btn-form-photo", function(){
    let tr = $(this).parents("tr")
    let id = tr.find(".id_hidden").html();
    console.log("asd")
    // get images
    getImagesUrls(id, addFormImages)

    $("#cat_id").val(id)
    closeAll()
    $(".form-conteiner").show();
    $(".form-close-bg").show();
});

$(".exit-icon").on( "click", function( event ) {
    closeAll()
});

$(".btn-exit").on( "click", function( event ) {
    closeAll()
});
$(".form-close-bg").on( "click", function( event ) {
    closeAll()
});

function addFormImages(result, id) {
    // /image/<int:cat_id>/<path></path>
    urls = result.result
    image_list = $(".image-list")
    image_list.html("")
    if (result.status != "ok") {
        return 
    }
    urls.forEach(element => {
        console.log(element)
        src = `'/image/${id}/${element}'`
        image_list.append(
        `<div class="image-item">
            <img src='/image/${id}/${element}' width="256px" height="256px">
            <button class='btn btn-danger btn-xs btn-delete-photo'>Delete</button>
        </div>`);
    });
}

function getImagesUrls(cat_id, func) {
    $.ajax({
        type: "GET",
        url: "/getImages/"+cat_id,
        // contentType: "application/json",
        // dataType: 'json',
        success: function(result) {
            func(result, cat_id)
            console.log(result.status)
        }
    });
}