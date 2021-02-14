// Ingredient popover for the pizzas
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
})

/* To select the item that you want to add to an offer.
This will outline which item you have selected, unhide those items and then scroll down to them.*/

$('.btn-selector').click(function(event){
    event.preventDefault()
    $('.offer-card').removeClass("selected-offer");
    $(this).parent().parent().toggleClass("selected-offer");
    let offerItem = $(this).data("offer-item").toLowerCase();
    $('.product-area').addClass("d-none");
    $('#' + offerItem).toggleClass("d-none");
    $("body,html").animate(
      {
        scrollTop: $("#" + offerItem).offset().top - 168
      },
      400 //speed
    );
})

/* To select the respective item and allocate it to the offer item section
Will then remove the view of other items.
*/

$('.item-selector').click(function(){
    let itemID = $(this).attr('id');
    let itemImage = $(this).data("item-image");
    let itemNumber = $('.selected-offer').data('item-number');
    let itemSize = $('.selected-offer').data('item-size');
    let itemName = $(this).data("item-name");
    $('.selected-offer').find("img").attr("src", itemImage);
    if (itemSize !== 'None')
        $('.selected-offer').find("h5").html(`${itemName} (${itemSize})`);
    else
        $('.selected-offer').find("h5").html(`${itemName}`);
    $('.selected-offer').find("img").removeClass("d-none");
    $('.selected-offer').find("img").siblings().addClass("d-none");
    $('.selected-offer').find("select").parent().removeClass("d-none");
    $('#select-btn-' + itemNumber).addClass("d-none");
    $('#change-btn-' + itemNumber).removeClass("d-none");
    $('.offer-card').removeClass("selected-offer");
    $('.product-area').addClass("d-none");
    $(`input[name="item${itemNumber}"]`).attr('value', itemID)
})

// Check on the form that something has been selected for each offer item.
var form = $('#add_offer_to_bag')

form.submit(function(ev){
    $('.offer-error').html("")
    let item1 = $('#item1').val()
    let item2 = $('#item2').val()
    let item3 = $('#item3').val()

    if (item1 == "" | item2 == "" | item3 == "" ){
        ev.preventDefault();
        let errorDiv = $('.offer-error');
        let html = `<p class="text-danger"><strong>You have not selected all items for your offer, please select all items to add to your order.</strong></p>`
        $(errorDiv).html(html);
        return
    }
})

