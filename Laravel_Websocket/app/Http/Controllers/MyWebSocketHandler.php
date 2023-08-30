<?php

namespace App\Http\Controllers;

use BeyondCode\LaravelWebSockets\WebSockets\Messages\PusherMessageFactory;
use BeyondCode\LaravelWebSockets\WebSockets\WebSocketHandler;
use Ratchet\ConnectionInterface;
use Ratchet\RFC6455\Messaging\MessageInterface;

// use Ratchet\WebSocket\MessageComponentInterface;
class MyWebsocketHandler extends WebSocketHandler
// class MyWebSocketHandler implements MessageComponentInterface
{

    // public function onOpen(ConnectionInterface $connection)
    // {
    //     // TODO: Implement onOpen() method.
    // }
    
    // public function onClose(ConnectionInterface $connection)
    // {
    //     // TODO: Implement onClose() method.
    // }

    // public function onError(ConnectionInterface $connection, \Exception $e)
    // {
    //     // TODO: Implement onError() method.
    // }

    public function onMessage(ConnectionInterface $connection, MessageInterface $message)
    {
        // TODO: Implement onMessage() method.
        var_dump(json_decode($message->getPayload()));

        $message = PusherMessageFactory::createForMessage($message, $connection, $this->channelManager);

        $message->respond();
    }
}