// add the form select for Bootstrap 5 which crispy forms does not handle

$(document).ready(function(){
    $('select').addClass('form-select')
})

// Bootstap 5 own code to activate the toast messages

var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl)
})
toastList.forEach(toast => toast.show());

// Django's own code for getting the CSRF Token

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// This determines whether the client has selected the collection or the delivery option. Updates to the Django seesion variable is changed.

$('.collection-select').click(function(){
    let request = new Request(
        '/checkout/update_delivery_or_collection/?delivery=collection',
        {headers: {'X-CSRFToken': csrftoken}}
    );
    
    fetch(request, {
            method: 'POST',
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        }).then(function(response) {
            $('.delivery-select').removeClass('btn-primary');
            $('.delivery-select').addClass('btn-secondary');
            $('.collection-select').removeClass('btn-secondary');
            $('.collection-select').addClass('btn-primary');
        });
})

$('.delivery-select').click(function(){
    let request = new Request(
        '/checkout/update_delivery_or_collection/?delivery=delivery',
        {headers: {'X-CSRFToken': csrftoken}}
    );
    fetch(request, {
            method: 'POST',
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        }).then(function(response) {
            $('.collection-select').removeClass('btn-primary');
            $('.collection-select').addClass('btn-secondary');
            $('.delivery-select').removeClass('btn-secondary');
            $('.delivery-select').addClass('btn-primary');
        });
})
