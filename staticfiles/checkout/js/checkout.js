// making sure that the delivery info is filled out correctly before moving on to the payment section.

$('.btn-payment').click(function(){
    var valid = true
    $('.fieldset-delivery').find('select, input').each(function(){
        if ($(this).prop('required')){
            if ($(this).val() !== ''){
                valid = true
            } else {
                valid = false
                $(this).focus()
                return false
            }
        }
    })
    console.log(valid)
    if(valid){
            $('.personal-info').removeClass('d-none');
            $('.delivery').addClass('d-none');
        }
})

$('.collection-select').click(function(event){
    event.preventDefault();
    location.reload();
})
$('.delivery-select').click(function(){
    event.preventDefault();
    location.reload();
})

// Adjusting the address on the payment view of the checkout form

// Update if the user is signed up and address automatically input
$('.fieldset-delivery').find('select, input').each(function(){
    updateAddress(this)
})

// update for any changes
$('.fieldset-delivery').find('select, input').change(function(){
    updateAddress(this)
})

function updateAddress(item){
    var name = $(item).attr('name')
    var value = $(item).val()
    $('.' + name).html(value)
    if (name === 'street_address2' && value == ""){
        $('.' + name).parent().addClass('d-none')
    } else {
        $('.' + name).parent().removeClass('d-none')
    }

}

// Stripe required JS

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    // var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrftoken,
        'client_secret': clientSecret,
        'save-info': saveInfo,
    }
    var url= 'cache_checkout_data/';

    $.post(url, postData).done(function(){
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                }
            }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
            // The payment has been processed!
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                    // Show a success message to your customer
                    // There's a risk of the customer closing the window before callback
                    // execution. Set up a webhook or plugin to listen for the
                    // payment_intent.succeeded event that handles any business critical
                    // post-payment actions.
                }
            }
        })
    }).fail(function(){
        location.reload();
    })
});

// end of Stripe JS





