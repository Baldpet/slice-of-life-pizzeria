// To hide the size parameters when the form first loads
$('.item-size').addClass('d-none');

//If Pizza is selcted as an item then to unhide the size element for that specific item.
$('.item-selector').change(function(){
    itemId = $(this).children().children('label').attr('for')
    itemSize = 'div_' + itemId + '_size'
    category = $('#' + itemId).val()
    console.log(itemSize)
    if ( category === '1'){
        $('#'+ itemSize).parent().removeClass('d-none')
    } else {
        $('#'+ itemSize).parent().addClass('d-none')
    }  
})

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

    if (category1 === '1') {
        if (size1 == "" | size1 == "NA"){
            e.preventDefault();
            let errorDiv = $('.item1-error');
            let html = `<p class="text-danger">You must select a size for the Pizza Offer Item.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_item1').offset().top) - 250
            }, 500);
            return
        }
    }
    if(category2 === '1' ){
        if (size2 == "" | size2 == "NA"){
            e.preventDefault();
            let errorDiv = $('.item2-error');
            let html = `<p class="text-danger">You must select a size for the Pizza Offer Item.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_item2').offset().top) - 250
            }, 500);
            return
        }
    }
    if(category3 === '1' ){
        if (size3 == "" | size3 == "NA"){
            e.preventDefault();
            let errorDiv = $('.item3-error');
            let html = `<p class="text-danger">You must select a size for the Pizza Offer Item.</p>`
            $(errorDiv).html(html);
            $('html, body').animate({
                scrollTop: ($('#id_item3').offset().top) - 250
            }, 500);
            return
        }
    } 
})
