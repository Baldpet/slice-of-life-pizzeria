// Fetches the current status of the order and updates the webpage to show the user the relevent stage.

let orderId = $('#title').data('orderid');
let url = `../../ordertracker/order_status?orderId=${orderId}`;
    
fetch(url).then(response => {
        return response.json();
    })
    .then(data => {
        status = data.status;
        if ( status == 'PR' ) {
            $('#preparing-frame').removeClass('d-none');
        } else if ( status == 'C' ) {
            $('#cooking-frame').removeClass('d-none');
        } else if ( status == 'OD' ) {
            $('#delivering-frame').removeClass('d-none');
        } else {
            $('#preparing-frame').removeClass('d-none');
        }
    }).catch(function(err){
        console.log(err);
    });

// refreshes the page every 2 mins to keep the status up to date.

setTimeout("location.reload();", 120000);