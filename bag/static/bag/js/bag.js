// Update quantity on click
$('.update-link').click(function(e){
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function(e){
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('product_size');
    var dough = $(this).data('dough');
    var url = `/bag/remove_item/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrftoken, 'product_size': size, 'dough': dough };

    $.post(url, data)
        .done(function(){
            location.reload();
        });
})

// Add Loyalty Discount
$('#loyalty-btn').click(function(e){
    let url = `/bag/loyalty_points/add/`;
    let data = {'csrfmiddlewaretoken': csrftoken };
    $.post(url, data)
        .done(function(){
            location.reload();
        });
})

// Remove Loyalty Discount

$('#loyalty-stop-btn').click(function(e){
    let url = `/bag/loyalty_points/remove/`;
    let data = {'csrfmiddlewaretoken': csrftoken };
    $.post(url, data)
        .done(function(){
            location.reload();
        });
})