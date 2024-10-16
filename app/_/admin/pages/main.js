(function() {
	const response = {
		data: {
			type: "page",
			title: "仪表盘",
			body: {
				"type": "log",
				"height": 300,
				"source": "/_api_/logs"
			  }
		},
		status: 0
	}

	window.jsonpCallback && window.jsonpCallback(response);
})();
