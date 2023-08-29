<?php

namespace App\Events;
namespace App;

use App\User;
use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;


use Ratchet\ConnectionInterface;
use Ratchet\RFC6455\Messaging\MessageInterface;
use Ratchet\WebSocket\MessageComponentInterface;


class MyEvent implements ShouldBroadcast 
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public $user;
    public $message;

    /**
     * Create a new event instance.
     *
     * @return void
     */
    public function __construct($message,User $user)
    {
        $this->message = $message;
        $this->user = $user;
    }

    /**
     * Get the channels the event should broadcast on.
     *
     * @return \Illuminate\Broadcasting\Channel|array
     */
    public function broadcastOn()
    {
        // return new Channel('my-channel');
        return new PrivateChannel('user.'.$this->user->id);
        // return new PrivateChannel('channel-name');
        // return['my-channel'];
    }

    public function broadcastAs()
    {
        return 'server.created';
        // return 'my-event';
    }

    public function broadcastWith()
    {
        // return ['id' => $this->user->id];
        return['message' => $this->message, 'status' => 'ok'];
    }

}

// class MyCustomWebSocketHandler implements MessageComponentInterface
// {

//     public function onOpen(ConnectionInterface $connection)
//     {
//         // TODO: Implement onOpen() method.
//     }
    
//     public function onClose(ConnectionInterface $connection)
//     {
//         // TODO: Implement onClose() method.
//     }

//     public function onError(ConnectionInterface $connection, \Exception $e)
//     {
//         // TODO: Implement onError() method.
//     }

//     public function onMessage(ConnectionInterface $connection, MessageInterface $msg)
//     {
//         // TODO: Implement onMessage() method.
//     }
// }