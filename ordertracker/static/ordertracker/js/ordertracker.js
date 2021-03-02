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

