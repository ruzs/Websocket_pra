<?php

namespace App\Http\Controllers;

use BeyondCode\LaravelWebSockets\WebSockets\Messages\PusherMessageFactory;
use BeyondCode\LaravelWebSockets\WebSockets\WebSocketHandler;
use Illuminate\Broadcasting\PrivateChannel;
// use BeyondCode\LaravelWebSockets\Server\WebSocketHandler;
use Ratchet\ConnectionInterface;
use Ratchet\RFC6455\Messaging\MessageInterface;
use App\Entities\User;

// use Ratchet\WebSocket\MessageComponentInterface;
class MyWebsocketHandler extends WebSocketHandler
// class MyWebsocketHandler implements MessageComponentInterface
{

    private $user;

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
        
        $payload=json_decode($message->getPayload());
        var_dump($payload->event,$payload);
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
        // var_dump($send_data);
        // var_dump(json_encode($send_data));
        
        if ($payload->event !='pusher:ping' && $payload->event !='pusher:pong' && $broadcast_channels) {
            foreach ($broadcast_channels->getSubscribedConnections() as $broadcast_channel) {
                $broadcast_channel->send(json_encode($send_data));
            }
        }

        // if ($payload->event == 'pusher:subscribe') {
        //     $send_data=[
        //         'event'=>'close',
        //         'data'=>[
        //             'name'=>$user->name,
        //         ],
        //     ];
        //     foreach ($broadcast_channels->getSubscribedConnections() as $broadcast_channel) {
        //         $broadcast_channel->send(json_encode($send_data));
        //     }
        // }

        if ( $payload->event == 'Send_Message' && isset($payload->data->Message)) {
            if ($payload->data->Message == "subscription_succeeded") {
                $user=User::where('name',$payload->data->Name)->first();
                $user->socketId=$payload->data->socketId;
                $user->save();
            }
        }
    }

    public function onClose(ConnectionInterface $connection)
    {
        $this->channelManager->removeFromAllChannels($connection);
        // dd($this->channelManager->getConnectionCount($connection->app->id));

        var_dump('close');
        // var_dump($connection);
        // $send_data->a='20';
        // $send_data=$connection->socketId;
        var_dump($connection->socketId);
        // echo($connection->socketId);
        // echo(gettype($connection->socketId));
        $user=User::where('socketId',$connection->socketId)->first();
        // $send_data='eddie'.$connection->socketId;
        // dd($send_data,$this->channelManager->getConnectionCount($connection->app->id));
        if ($this->channelManager->getConnectionCount($connection->app->id)>0) {
            if ($user) {
                $send_data=[
                    'event'=>'close',
                    'data'=>[
                        'name'=>$user->name,
                    ],
                ];
                $broadcast_channels = $this->channelManager->find($connection->app->id, 'private-order.20');
                foreach ($broadcast_channels->getSubscribedConnections() as $broadcast_channel) {
                    $broadcast_channel->send(json_encode($send_data));
                }
            }
        }
        // $user->socketId=null;
        // $user->save();
    }
}