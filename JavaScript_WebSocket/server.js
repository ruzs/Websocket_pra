//import express 和 ws 套件
const express = require('express')
const SocketServer = require('ws').Server
const PORT = 3000 //指定 port
var chat='';
//創建 express 物件，綁定監聽  port , 設定開啟後在 console 中提示
const server = express().listen(PORT, () => {
    console.log(`Listening on ${PORT}`)
})
//將 express 交給 SocketServer 開啟 WebSocket 的服務
const wss = new SocketServer({ server })
//當有 client 連線成功時
wss.on('connection', ws => {
  console.log('Client connected');
  // 當收到client消息時
  ws.on('message', data => {
    // 收回來是 Buffer 格式、需轉成字串
    data = data.toString();
    token= ',000913';
    data=data.split(token);
    console.log('data2',data); // 可在 terminal 看收到的訊息
    data=`${data[1]}:${data[0]}`;
    // chat= chat+data;
    /// 發送消息給client 
    // ws.send(data)

    /// 發送給所有client： 
    let clients = wss.clients  //取得所有連接中的 client
    clients.forEach(client => {
      // console.log('client',client);
      client.send(data)  // 發送至每個 client
    })
  })
  // 當連線關閉
  ws.on('close', () => {
    console.log('Close connected')
  })
})