
function make_cotization(price_class, quantity_class, cotization_id){
    prices = document.getElementsByClassName(price_class);
    quantities = document.getElementsByClassName(quantity_class);
    total = 0;
    for (let index = 0; index < prices.length; index++) {
        if(quantities[index].value != '' && quantities[index].value > 0){
        total = total + parseFloat(prices[index].innerText)*quantities[index].value;}
        
    }

    document.getElementById(cotization_id).innerText = 'El monto seria: '+total.toFixed(2);

}