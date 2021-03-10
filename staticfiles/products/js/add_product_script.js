// Removes the Pizza only options from form rendering.
$('.pizza-only').addClass('d-none');

//Removes the price tables from rendering
$('.pizza_price').addClass('d-none');
$('.side_price').addClass('d-none');
$('.drink_price').addClass('d-none');
$('.premium').addClass('beige');

// If it is a amend will render the correct elements for what the item has already selected

$(document).ready(function(){
    let category = $('#id_category').val();
    if (category === '1') {
        $('.pizza-only').removeClass('d-none');
    }
    categoryCheck(category);
    let isPremium = $('#div_id_is_premium').children('input')[0].checked;
    premiumCheck(isPremium);
})

// If Pizza is selected in the Category, Adds the Pizza only options to the form rendering.
$('#id_category').change(function(){
    let category = $(this).val();
    if (category === '1') {
        $('.pizza-only').removeClass('d-none');
    } else {
        $('.pizza-only').addClass('d-none');
    }
})

// Adds the relevant price table when a certain category is selected
$('#id_category').change(function(){
    let category = $(this).val();
    categoryCheck(category)
    
})

$('#id_is_premium').click(function(){
    isPremium = this.checked
    premiumCheck(isPremium)
})

// Functions foe checking the category and the premium price

function categoryCheck(category) {
    if (category === '1') {
        $('.side_price').addClass('d-none');
        $('.drink_price').addClass('d-none');
        $('.pizza_price').removeClass('d-none');
    } else if(category === '2') {
        $('.pizza_price').addClass('d-none');
        $('.drink_price').addClass('d-none');
        $('.side_price').removeClass('d-none');
    } else if(category === '3') {
        $('.pizza_price').addClass('d-none');
        $('.side_price').addClass('d-none');
        $('.drink_price').removeClass('d-none');
    } else {
        $('.side_price').addClass('d-none');
        $('.drink_price').addClass('d-none');
        $('.pizza_price').addClass('d-none');
    }
}

function premiumCheck(isPremium){
    console.log(isPremium)
    if(isPremium){
        $('.non-premium').removeClass('beige')
        $('.premium').addClass('beige')
    } else {
        $('.premium').removeClass('beige')
        $('.non-premium').addClass('beige')
    }
}

// Validates the form to make sure that a Base, Sauce and Cheese element is selected before submission.
// This validation is only when Pizza is selected in the category.
var form = $('#product');

form.submit(function(e){
    
    let category = $('#id_category').val();
    let dough = $('#id_dough').val();
    let sauce = $('#id_sauce').val();
    let cheese = $('#id_cheese').val();
    console.log(`${category}, ${dough}, ${sauce}, ${cheese},`)

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
  