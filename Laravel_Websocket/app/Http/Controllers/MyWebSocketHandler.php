<?php

namespace App\Http\Controllers;

use BeyondCode\LaravelWebSockets\WebSockets\Messages\PusherMessageFactory;
use BeyondCode\LaravelWebSockets\WebSockets\WebSocketHandler;
use Illuminate\Broadcasting\PrivateChannel;
// use BeyondCode\LaravelWebSockets\Server\WebSocketHandler;
use Ratchet\ConnectionInterface;
use Ratchet\RFC6455\Messaging\MessageInterface;

// use Ratchet\WebSocket\MessageComponentInterface;
class MyWebsocketHandler extends WebSocketHandler
// class MyWebsocketHandler implements MessageComponentInterface
{
    // public function onOpen(ConnectionInterface $connection)
    // {
    //     // TODO: Implement onOpen() method.
    // }

    // public function onError(ConnectionInterface $connection, \Exception $e)
    // {
    //     // TODO: Implement onError() method.
    // }

    public function onMessage(ConnectionInterface $connection, MessageInterface $message)
    {
        parent::onMessage($connection, $message);
        
        // var_dump(json_decode($message->getPayload()));
        $payload=json_decode($message->getPayload());
        // var_dump($payload->event);
        // dd($payload->event);
        // if ($payload->event=='Send_Message') {
        //     echo $payload->event;
        // }
        // var_dump($payload->data);
        // $allChat=[];
        // array_push($allChat, $payload);
        // var_dump($allChat);
        $broadcast_channels = $this->channelManager->find($connection->app->id, 'private-order.20');
        // $broadcast_channels = $this->channelManager->find('room', 'private-order.20');

        // var_dump($broadcast_channels);
        
        $send_data=$payload;

        // if ($payload->event !='pusher:subscribe' && $payload->event !='pusher:ping' && $broadcast_channels) {
        if ($payload->event !='pusher_internal:subscription_succeeded' && $payload->event !='pusher:ping' && $payload->event !='pusher:pong' && $broadcast_channels) {

            foreach ($broadcast_channels->getSubscribedConnections() as $broadcast_channel) {
                $broadcast_channel->send(json_encode($send_data));
            }

        }

        // $broadcast_channels = $this->channelManager->find('pusher app id', 'channel name');
        // if ($broadcast_channels) {
        //     foreach ($broadcast_channels->getSubscribedConnections() as $broadcast_channel) {
        //         $broadcast_channel->send(json_encode($send_data));
        //     }
        // }
    }

    // public function onClose(ConnectionInterface $connection)
    // {
    //     $this->channelManager->removeFromAllChannels($connection);

    //     var_dump('close');
    // }
}