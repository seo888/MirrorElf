(function () {
	const response = {
		data: {
			"type": "page",
			"title": "缓存管理",
			"toolbar": [

			],

			"body": {
				"type": "crud",
				"id": "crud-table",
				"syncLocation": false,
				// "quickSaveApi": "/_api_/website_cache/update?id=${id}",  // 更新 API 地址
				"draggable": true,
				"api": "/_api_/website_cache/query",
				"perPage": 20,
				"keepItemSelectionOnPageChange": true,
				"autoFillHeight": true,
				"labelTpl": "【${id}】",
				"autoGenerateFilter": true,
				"bulkActions": [
					{
						"label": "批量删除",
						"level": "danger",
						"actionType": "ajax",
						"api": "delete:/_api_/website_cache/delete?ids=${ids|raw}",
						"confirmText": "确认批量删除URL【${ids|raw}】（注意：操作不可逆，请谨慎操作）"
					}
				],
				"filterTogglable": true,
				"headerToolbar": [
					"bulkActions",
					{
						"type": "tpl",
						"tpl": "URL总数: ${total_count}",
						"className": "v-middle"
					},
					{
						"type": "columns-toggler",
						"align": "right"
					},
					{
						"type": "drag-toggler",
						"align": "right"
					},
					{
						"type": "pagination",
						"align": "right"
					},
					{
						"type": "tpl",
						"tpl": "当前：${items_count} 项 | 共：${count} 项",
						"align": "right"
					}
				],
				"footerToolbar": [
					"statistics",
					{
						"type": "pagination",
						"layout": "perPage,pager,go"
					}
				],
				"columns": [
					{
						"name": "id",
						"label": "ID",
						"searchable": {
							"type": "input-text",
							"name": "search_term",
							"label": "🔍搜索",
						},
						"fixed": "left",
						"sortable": true,  // 启用排序功能
					},

					{
						"type": "tpl",
						"tpl": "<a href='javascript:void(0);' class='link-icon' target='_blank'>${url}</a>",
						"name": "url",
						"label": "网站URL",
						"sortable": true,
						"searchable": true,
						"onEvent": {
							"click": {
								"actions": [
									{
										"actionType": "custom",
										"script": "const parts = event.data.url.split('['); if(parts.length > 0) { const linkTarget = parts[0]; document.querySelector('.link-icon').setAttribute('href', 'http://' + linkTarget); window.open('http://' + linkTarget, '_blank'); }"
									}
								]
							}
						}
					},
					{
						"name": "lang",
						"label": "语言",
						"sortable": true,  // 启用排序功能
						"searchable": true,
					},
					{
						"type": "tpl",
						"tpl": "<a href='javascript:void(0);' class='link-icon' target='_blank'>${target}</a>",
						"name": "target",
						"label": "目标站",
						"sortable": true,
						"searchable": true,
						"onEvent": {
							"click": {
								"actions": [
									{
										"actionType": "custom",
										"script": "const parts = event.data.url.split('['); if(parts.length > 0) { const linkTarget = parts[0]; document.querySelector('.link-icon').setAttribute('href', 'http://' + linkTarget); window.open('http://' + linkTarget, '_blank'); }"
									}
								]
							}
						}
					},
					{
						"name": "title",
						"label": "标题",
						"sortable": true,  // 启用排序功能
						"searchable": true,
					},
					{
						"name": "keywords",
						"label": "关键词",
						"sortable": true,  // 启用排序功能
						"searchable": true,
					},
					{
						"name": "description",
						"label": "描述",
						"sortable": true,  // 启用排序功能
						"searchable": true,
					},
					{
						"type": "tpl",
						"tpl": "<a href='http://${domain}' target='_blank' class='link-style'>${domain}</a>",
						"name": "domain",
						"label": "域名",
						"fixed": "left",
						"searchable": true,
						"sortable": true
					},
					{
						"name": "root_domain",
						"label": "根域名",
						"sortable": true,  // 启用排序功能
						"searchable": true,
					},
					// {
					// 	"name": "source",
					// 	"label": "源码",
					// 	"sortable": true,  // 启用排序功能
					// 	// "searchable": true,
					// },
					{
						"type": "datetime",  // 显示为日期时间类型
						"name": "updated_at",
						"label": "更新于",
						"sortable": true,  // 启用排序功能
					},
					{
						"type": "operation",
						"label": "操作",
						"width": 60,
						"buttons": [
							{
								"type": "button",
								"icon": "fa fa-eraser text-danger",
								"actionType": "ajax",
								"tooltip": "清空根域名缓存",
								"confirmText": "确认清空 根域名:${root_domain} 及所有 泛域名:*.${root_domain} 所有页面缓存",
								"api": "delete:/_api_/website_cache/delete?root_domain=$root_domain",
							},
							{
								"type": "button",
								"icon": "fa fa-pencil",
								"tooltip": "编辑",
								"actionType": "drawer",
								"drawer": {
									"size": "lg",
									"title": "编辑",
									"body": {
										"type": "form",
										"name": "sample-edit-form",
										"api": "/_api_/website/update?id=$id",
										"reload": "crud-table", // 在提交后重新加载特定的组件
										"body": [
											{
												"type": "static",
												"name": "url",
												"label": "网站URL",

											},
											{
												"type": "static",
												"name": "lang",
												"label": "语言",
												"required": true
											},
											{
												"type": "static",
												"name": "target",
												"label": "目标站",
											},
											// {
											// 	"type": "static-mapping",
											// 	"name": "is_www",
											// 	"label": "站点类型",
											// 	"map": {
											// 		"true": "主站",
											// 		"false": "泛站"
											// 	}
											// },
											// {
											// 	"type": "input-text",
											// 	"name": "target",
											// 	"label": "目标站",
											// 	"required": true,
											// 	"placeholder": "目标站格式: en|www.english.com",
											// 	"validations": {
											// 		"matchRegexp": ".*\\|.*"  // 正则表达式：要求输入中必须包含 "|"
											// 	},
											// 	"validationErrors": {
											// 		"matchRegexp": "请使用间隔符“|” 指定目标站语言 如: en|www.english.com  或  zh|www.chinese.com"  // 自定义错误提示信息
											// 	}
											// },
											// 插入新的 service，用于加载 target_replace 数据
											{
												"type": "input-text",
												"name": "title",
												"label": "网站标题",
												"required": true
											},
											{
												"type": "input-text",
												"name": "keywords",
												"label": "关键词"
											},
											{
												"type": "textarea",
												"name": "description",
												"label": "描述"
											},
											{
												"type": "static",
												"name": "domain",
												"label": "域名"
											},
											{
												"type": "static",
												"name": "root_domain",
												"label": "根域名"
											},
											{
												"type": "service",
												"api": "/_api_/website_cache/get_source?url=$url",  // 动态加载 target_replace 数据的 API
												"body": [
													{
														"type": "editor",
														"language": "html",
														"name": "source",
														"label": "目标站替换词",
													}
												]
											},
											{
												"type": "static",
												"name": "created_at",
												"label": "创建于"
											},
											{
												"type": "static",
												"name": "updated_at",
												"label": "更新于"
											}
										]
									}
								}
							},
							{
								"type": "button",
								"icon": "fa fa-eraser text-danger",
								"actionType": "ajax",
								"tooltip": "清空当前域名缓存",
								"confirmText": "确认清空 域名:${domain} 所有页面缓存",
								"api": "delete:/_api_/website_cache/delete?domain=$domain",
							},
							{
								"icon": "fa fa-times text-danger",
								"actionType": "ajax",
								"confirmText": "确认删除【${id}】${url}",
								"api": "delete:/_api_/website_cache/delete?ids=$id",
							},
						],
						"toggled": true
					}
				]
			}
		},
		status: 0
	}

	window.jsonpCallback && window.jsonpCallback(response);
})();
