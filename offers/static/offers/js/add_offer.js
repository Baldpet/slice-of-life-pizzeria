// To hide the size parameters when the form first loads unless Pizza is selected
$(document).ready(function(){
    $('.item-size').addClass('d-none');
    $('.item-selector').each(function(){
        let itemId = $(this).children().children('label').attr('for');
        activateSize(itemId)
    })
})

//If Pizza is selcted as an item then to unhide the size element for that specific item.
$('.item-selector').change(function(){
    let itemId = $(this).children().children('label').attr('for');
    activateSize(itemId)
})

function activateSize(itemId){
    let itemSize = 'div_' + itemId + '_size'
    let category = $('#' + itemId).val()
    if ( category === '1'){
        $('#'+ itemSize).parent().removeClass('d-none')
    } else {
        $('#'+ itemSize).parent().addClass('d-none')
    }  
}

//On submit checks to see that a size has been selected if the item is a Pizza.

var form = $('#add_offer_form')

form.submit(function(e){
    $('.item1-error').html("")
    $('.item2-error').html("")
    $('.item3-error').html("")
    
    let category1 = $('#id_item1').val();
    let category2 = $('#id_item2').val();
    let category3 = $('#id_item3').val();
    let size1 = $('#id_item1_size').val();
    let size2 = $('#id_item2_size').val();
    let size3 = $('#id_item3_size').val();
    let errorDiv1 = $('.item1-error');
    let errorDiv2 = $('.item2-error');
    let errorDiv3 = $('.item3-error');

    errorCheck(size1, category1, errorDiv1);
    errorCheck(size2, category2, errorDiv2);
    errorCheck(size3, category3, errorDiv3);
 
})

function errorCheck(category, size, errorDiv) {
    if(category === '1' ){
        if (size == "" | size == "NA"){
            e.preventDefault();
            let html = `<p class="text-danger">You must select a size for the Pizza Offer Item.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_item3').offset().top) - 250
            }, 500);
            return
        }
    } 
}
