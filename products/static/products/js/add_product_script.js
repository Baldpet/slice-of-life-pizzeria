// Removes the Pizza only options from form rendering.
$('.pizza-only').addClass('d-none');

// If Pizza is selected in the Category, Adds the Pizza only options to the form rendering.
$('#id_category').change(function(){
    let category = $(this).val();
    if (category === '1') {
        $('.pizza-only').removeClass('d-none');
    } else {
        $('.pizza-only').addClass('d-none');
    }
})

// Validates the form to make sure that a Base, Sauce and Cheese element is selected before submission.
// This validation is only when Pizza is selected in the category.
var form = $('#add_product_form');

form.submit(function(e){
    
    let category = $('#id_category').val();
    let dough = $('#id_dough').val();
    let sauce = $('#id_sauce').val();
    let cheese = $('#id_cheese').val();

    if (category === '1') {
        if (dough == ""){
            e.preventDefault();
            let errorDiv = $('.pizza_error_div_dough');
            let html = `<p class="text-danger">You must select a Dough Type for a Pizza Product.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_dough').offset().top) - 250
            }, 500);
            return
        } 
        if (sauce == ""){
            e.preventDefault();
            let errorDiv = $('.pizza_error_div_sauce');
            let html = `<p class="text-danger">You must select a Base Sauce for a Pizza Product.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_sauce').offset().top) - 250
            }, 500);
            return
        }
        if (cheese == ""){
            e.preventDefault();
            let errorDiv = $('.pizza_error_div_cheese');
            let html = `<p class="text-danger">You must select a Base Cheese for a Pizza Product.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_cheese').offset().top) - 250
            }, 500);
            return
        }
    } 
})
    