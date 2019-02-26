$(document).ready(function() {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('23');
        var nmb = $('#number').val();
        console.log(nmb)
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data('product_id')
        var product_name = submit_btn.data('name')
        var product_price = submit_btn.data('price')

        $('.basket-items ul').append('<li>' + product_name + ', ' + nmb + 'шт. ' + 'по ' + product_price + 'гр.  ' +
            '<a class="delete-item " href="">x</a>' +
            '</li>')

    });

    function shovingBasket(){
        $('.basket-items').toggleClass('d-none');
    }
    $('.basket-container').on('click',function (e) {
        e.preventDefault();
        shovingBasket()

    });

    $('.basket-container').mouseover('click',function () {
        shovingBasket()
    });

        // $('.basket-container').mouseout('click',function () {
        //     shovingBasket()
        // });
    $(document).on('click','.delete-item',function (e) {
        e.preventDefault()
        $(this.closest('li')).remove()
        
    })




});