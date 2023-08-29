<?php

use Illuminate\Support\Facades\Route;
use BeyondCode\LaravelWebSockets\Facades\WebSocketsRouter;
use BeyondCode\LaravelWebSockets\WebSockets\Channels\Channel;
use BeyondCode\LaravelWebSockets\WebSockets\Channels\PrivateChannel;

// WebSocketsRouter::webSocket('/app', YourWebSocketHandler::class);
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('websocket');
});

// Route::get('/test', function () {
//     return event(new \App\Events\MyEvent('hello world'));
// })->name('test');

// function onMessage(ConnectionInterface $connection, MessageInterface $message)
// {
//     $data = json_decode($message->getContent(), true);

//     if ($data['event'] === 'chat.message') {
//         $channel = new PrivateChannel('chat.' . $data['channel_id']);

//         $this->broadcastToChannel($channel, [
//             'event' => 'chat.message',
//             'data' => $data['message'],
//         ]);
//     }
// }