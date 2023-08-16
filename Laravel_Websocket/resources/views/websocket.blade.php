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
                height: 100vh;
                margin: 0;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                text-align: center;
            }

            .title {
                font-size: 84px;
            }

            .links > a {
                color: #636b6f;
                padding: 0 25px;
                font-size: 13px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
            }

            .m-b-md {
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body>
        <div class="block m-4">
            <textarea cols="50" rows="10" id="txtShow" disabled></textarea>
            <input id="txtInput" type="text">
            <input type="submit" id="btnSend" value="送出">
            <br>
            <div id="idn">ID=</div>
        </div>

        <div class="flex-center position-ref full-height">
            <div class="top-right links">
                <a href="">Home</a>
                <a href="">Login</a>
                <a href="">Register</a>
            </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.min.js" integrity="sha512-3gJwYpMe3QewGELv8k/BX9vcqhryRdzRMxVfq6ngyWXwo03GFEzjsUm8Q7RZcHPHksttq7/GFoxjCVUjkjvPdw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
        <script src="../js/app.js"></script>
        <script>
            // let url = 'ws://websocket.com.tw:6001';
            // var ws = new WebSocket(url);

            // ws.onopen = (event) => {
            //     console.log('open connection');
            //     hr = new Date().getHours() < 10 ? '0' + new Date().getHours() : new Date().getHours();
            //     min = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes();
            //     sec = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds();
            //     showDom.value = hr + ":" + min + ":" + sec + "|" + `${user}進入聊天室`;
            //     console.log('open_event', event);
            //     console.log('ws', ws);
            //     console.log('user', user);
            //     ws.send('a1a2a3a'+user);
            // }
            
            // import Echo from "../js/bootstrap"
            // // import Echo from "laravel-echo"
            // window.Pusher = require('pusher-js');
            // // console.log('key',process.env.MIX_PUSHER_APP_KEY);
            // window.Echo = new Echo({
            //     broadcaster: 'pusher',
            //     key: process.env.MIX_PUSHER_APP_KEY,
            //     cluster: process.env.MIX_PUSHER_APP_CLUSTER,
            //     forceTLS: false,
            //     disableStats: true,
            //     enabledTransports: ['ws', 'wss'],
            // });

            // console.log('window',WebSocket);
            // window.Echo.private(`chat`).listen('chat.message', (event) => {
            //     console.log(event.data);
            // });
            
        </script>
    </body>
</html>
