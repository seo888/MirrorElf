(function () {
	const response = {
		data: {
			"type": "page",
			"title": "实时日志查看",
			"body": {
				"type": "log",
				"name": "log",
				"height": 400,
				"source": {
					"type": "websocket",
					"url": "${window.location.host}/_api_/logs",
					"reconnect": true,
					"reconnectInterval": 3000
				}
			}
		},
		status: 0
	}

	window.jsonpCallback && window.jsonpCallback(response);
})();
