// Adds the pizza choices for the select options to the table summary

$('#create-pizza-form select').change(function(){
    let item = $(this).attr('name');
    let pizzaItem = 'pizza-' + item;
    let value = $(this).val();
    $('.' + pizzaItem).html(value);
    let baseCost = 6.00;
    let cost = 0;
    if (item === 'size'){
        baseCost = $(':selected', this).data("cost");
        $('.' + pizzaItem).next().html('£' + baseCost);
    }
    let count = $('.form-check-inline :checked').length;
    cost = (count * 0.50).toFixed(2);
    let totalCost = (parseFloat(baseCost) + parseFloat(cost)).toFixed(2);
    $('#total-cost').html(`<strong>£${totalCost}</strong>`);
});

// Adds the toppings totals for the multiselect options to the table summary

$('.form-check-inline').change(function(){
    let baseCost = 0;
    let count = $('.form-check-inline :checked').length;
    $('.pizza-toppings').html(count);
    let cost = (count * 0.50).toFixed(2);
    $('.pizza-toppings').next().html('£' + cost);
    baseCost = parseFloat($('.pizza-size').next().html().slice(1));
    let totalCost = (baseCost + parseFloat(cost)).toFixed(2);
    $('#total-cost').html(`<strong>£${totalCost}</strong>`);
});