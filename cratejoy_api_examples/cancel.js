/*
	1. Put in your username and password.
	2. Update the call to be what you want.
	3. Run `node cancel.js`

	Or, more likely, change it so the object id and data aren't hardcoded. This is just examples to get you started.
*/

var https = require('https');

var host = 'api.cratejoy.com';
var username = 'client_user';
var password = 'client_secret';

function api_request(endpoint, method, data, success) {
	var auth = 'Basic ' + new Buffer(username + ':' + password).toString('base64')
	var headers = {
		'Content-Type': 'application/json',
		'Authorization': auth,
		'Content-Length': data.length
	};
	var args = {
		host: host,
		path: endpoint,
		method: method,
		headers: headers
	};

	var req = https.request(args, function(res) {
		res.setEncoding('utf-8');

		var response_string = '';

		res.on('data', function(data) {
			response_string += data;
		});

		req.on('error', function(e) {
			console.log('e='+e)
			deferred.reject(e);
		});

		res.on('end', function() {
			console.log('response=' + response_string);
		});
	});

	console.log(args);
	console.log(endpoint);
	console.log(data);
	req.write(data);
	req.end();
}

var sub_id = 720951477;

api_request('/v1/subscriptions/' + sub_id + '/cancel/', 'PUT', '{"cancel_reason":6, "log_note":"This is an API test."}', function(){})
