* [Using fetch to Make Network Requests](#vrr9c)
* [Using https to Make Requests](#oowx7)

1. [Developer Guide](/plugin-api/tutorial)
# Issue Network Requests

You can use the fetch method provided by web technologies or the native https module in Node.js to make network requests.

## Using `fetch` to Make Network Requests

The `fetch` function is a tool for accessing network resources, allowing you to send HTTP requests and handle response processing. The `fetch` function supports many different types of requests, including `GET`, `POST`, `PUT`, and `DELETE`, and supports custom formats for request and response bodies.

By using the `fetch` function, you can easily access network resources and control the request and response process. For example, you can use the following code to send a `GET` request and process the response after the request is fulfilled:

Copy
```
fetch('https://example.com/api/endpoint')
    .then(response => response.json())
    .then(data => {
    	// Process the response here
    });
```

This example code sends a GET request to the specified network resource, then parses the response body into JSON format after the request is completed, and processes the parsed response body here.

To learn more about the `fetch` function in Javascript, it is recommended to read the introduction on the MDN website:
<https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>.

This article introduces the basic usage of the `fetch` function and provides example code demonstrating how to use `fetch` to send HTTP requests and handle response processing.

In addition, you can refer to the following articles for more information about fetch:

* "Using Fetch" (<https://davidwalsh.name/fetch>)
* "Fetch API In Depth" (<https://css-tricks.com/using-fetch/>)

---

## Using `https` to Make Requests

Due to the default security limitations of browsers, the `fetch` method sometimes encounters some restrictions. In this case, we can switch to using Node.js native networking APIs to send network requests for greater flexibility.

Sending an HTTP GET request using the `https.get` method is very simple; you only need to provide the URL of the request. For example, you can use the following code to send an HTTP GET request:

Copy
```
const https = require('https');
https.get('https://www.example.com', (res) => {
  console.log(`Got response: ${res.statusCode}`);
  res.on('data', (d) => {
    // Process response data
  });
}).on('error', (e) => {
  console.error(`Got error: ${e.message}`);
});
```
[PreviousAccess Local Files](/plugin-api/tutorial/access-local-files)[NextUsing Node.js Native API](/plugin-api/tutorial/node-js-native-api)

Last updated 1 year ago