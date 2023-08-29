<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Websocket</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;600&display=swap" rel="stylesheet">
        
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <!-- Styles -->
        <style>
            html, body {
                background-color: #fff;
                color: #636b6f;
                font-family: 'Nunito', sans-serif;
                font-weight: 200;
                /* height: 100vh; */
                /* margin: 0; */
            }
        </style>
    </head>
    <body>
        <div class="mt-5">
            <div class="d-inline-block ml-5">
                <textarea class="d-inline-block" cols="50" rows="10" id="txtShow" disabled></textarea>
                <br>
                <div class="d-inline-block">
                    <div id="idn" class="d-inline-block">ID=</div>
                    <input type="text" id="txtInput" class="d-inline-block">
                    <input type="submit" id="btnSend" class="d-inline-block" value="送出">
                </div>
            </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.min.js" integrity="sha512-3gJwYpMe3QewGELv8k/BX9vcqhryRdzRMxVfq6ngyWXwo03GFEzjsUm8Q7RZcHPHksttq7/GFoxjCVUjkjvPdw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
        <script src="{{ asset('js/app.js') }}"></script>
        <script>
            let orderId = 20;
            let keyinDom = $('#txtInput');
            let showDom = $('#txtShow');


            $(document).on('click','#btnSend',function () {
                let txt = keyinDom.val();
                console.log('click',txt);
                Echo.private(`order${orderId}`)
                    .listen('ShippingStatusUpdated', (e) => {
                        console.log(e.update);
                    })
                    ;
                orderId+=1;
                console.log('Echo',Echo);
                keyinDom.val('');
            })


            $(document).on('keypress','#txtInput',function () {
                let txt = keyinDom.val();
                if (event.key === "Enter") {
                // if (event.which === 13) {
                    if (txt.length === 0 || txt.trim() == "") {
                    } else {
                        event.preventDefault();
                        // console.log('txt',txt);
                        $("#btnSend").click();
                    }
                }
            })

            console.log("                  _oo0oo_\n                 o8888888o\n                 88\" . \"88\n                 (| -_- |)\n                 0\\  \x3d  /0\n               ___/`---'\\___\n             .' \\\\|     |// '.\n            / \\\\|||  :  |||// \\\n           / _||||| -:- |||||- \\\n          |   | \\\\\\  -  /// |   |\n          | \\_|  ''\\---/''  |_/ |\n          \\  .-\\__  '-'  ___/-. /\n        ___'. .'  /--.--\\  `. .'___\n     .\"\" '\x3c  `.___\\_\x3c|\x3e_/___.' \x3e' \"\".\n    | | :  `- \\`.;`\\ _ /`;.`/ - ` : | |\n    \\  \\ `_.   \\_ __\\ /__ _/   .-` /  /\n\x3d\x3d\x3d\x3d\x3d`-.____`.___ \\_____/___.-`___.-'\x3d\x3d\x3d\x3d\x3d\n                  `\x3d---\x3d'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n          \u4f5b\u7956\u4fdd\u4f51         \u6c38\u7121BUG\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            
            // Echo.leave(`orders.${this.order}`);
            // const channel = window.Echo.join('orders');
            // channel.listen('EventName', (data) => {
            //     console.log('Event received:', data);
            // });

            // channel.leave();
        </script>
    </body>
</html>
