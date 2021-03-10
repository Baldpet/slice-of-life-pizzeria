// Adds colour to the orders list, if they are over 20 mins then a red warning, if over 10 mins but below 20 mins then orange.

$(document).ready(function(){
    $('.time').each(function(){
        var orderNumber = $(this).data('order');
        var time = $(this).data('time');
        if (time > 20){
            $('.' + orderNumber).addClass('background-red');  
        } else if (time > 10) {
            $('.' + orderNumber).addClass('background-orange');
        }  
    })
})

// refreshes the page automatically every minute to allow staff to keep track of orders

setTimeout("location.reload();", 60000)

// Update the order status and refresh the page

$('.btn-stage').click(function(){
    let buttonId = $(this).attr('id')
    let arrayButtonId = buttonId.split("-")
    let status = arrayButtonId[0]
    let orderId = arrayButtonId[1]
    let request = new Request(
        `order_status?status=${status}&orderId=${orderId}`,
        {headers: {'X-CSRFToken': csrftoken}}
    );
    
    fetch(request, {
            method: 'POST',
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        }).then(function(response) {
            location.reload()
        });
    
});

// enable popovers

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})



