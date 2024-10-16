(function() {
	const response = {
		data: {
			type: "page",
			title: "仪表盘",
			body: {
				"type": "log",
				"height": 300,
				'maxLength':200,
				"source": "/_api_/logs"
			  }
		},
		status: 0
	}

	window.jsonpCallback && window.jsonpCallback(response);
})();
