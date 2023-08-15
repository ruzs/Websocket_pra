//import express 和 ws 套件
const express = require('express')
const SocketServer = require('ws').Server
const PORT = 3000 //指定 port
var chat = [];
var chat_saved = [];
var i = 0;
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
		hr = new Date().getHours() < 10 ? '0' + new Date().getHours() : new Date().getHours();
		min = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes();
		sec = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds();
		time = hr + ":" + min + ":" + sec + "|";
		i++;
		// 收回來是 Buffer 格式、需轉成字串
		open_token='a1a2a3a';
		token = ',000913';
		close_token='z1z2z3z';
		data = data.toString();
		if (data.includes(open_token)) {
			// console.log('data',data);
			data = data.split(open_token);
			chat.push(`${time}${data[1]} 進入聊天室`);
			
		}
		if (data.includes(token)) {
			data = data.split(token);
			console.log('data2', data); // 可在 terminal 看收到的訊息
			data = `${time}${data[1]}: ${data[0]}`;
			chat.push(data);
		}

		if (data.includes(close_token)) {
			data = data.split(close_token);
			chat.push(`${time}${data[1]} 離開聊天室`);
		}

		/// 發送消息給client 
		// ws.send(data)

		/// 發送給所有client： 
		// let clients = wss.clients  //取得所有連接中的 client
		// clients.forEach(client => {
		// console.log('client',client);
		// client.send(data)  // 發送至每個 client
		// })
		if (i>=20) {
			// chat_save.push(chat[0]);
			// chat.shift();
			chat_saved.push(chat.shift());
			if (i%5 ==0) {
				console.log('000',chat_saved);
			}
		}


		let clients = wss.clients;
		clients.forEach(client => {
			chatS = chat.join('\n');
			client.send(chatS);
		})
		if (i%5 ==0) {
			
			console.log('chatS\n', chat.join('\n'));
		}
		// }

	})
	// 當連線關閉
	ws.on('close', () => {
		console.log('Close connected')
	})
})