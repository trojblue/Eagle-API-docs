* [Example](#oedfw)
* [Recommended Learning Resources](#unfm7)

1. [Developer Guide](/plugin-api/tutorial)
# Using Node.js Native API

The Eagle plugin supports the use of Node.js native APIs, allowing us to enjoy the following benefits:

* Leverage the powerful features of Node.js for complex functions such as data processing, file compression, and network communication.
* Utilize various modules and libraries from the existing Node.js ecosystem to quickly implement different functions in applications, avoiding reinventing the wheel.
* Build cross-platform applications since Node.js has great support on Windows and macOS.

## Example

Copy
```
const fs = require('fs');
// Read file
fs.readFile('/path/to/file.txt', (err, data) => {
    if (err) throw err;
    console.log(data);
});
// Write file
fs.writeFile('/path/to/file.txt', 'Hello, world!', (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
});

```

This code snippet reads a file and then writes a text to it. During the read and write operations, relevant information is displayed in the console.

In addition to the `fs` module, the Node.js native API offers many other useful modules that provide a range of common functions. Here are some popular Node.js native modules:

2. `http` module: Provides HTTP server and client functionality.
5. `path` module: Provides utility functions for handling file paths.
8. `os` module: Provides features to obtain operating system information.
11. `crypto` module: Offers encryption and decryption capabilities.
14. `zlib` module: Delivers data compression and decompression features.

## Recommended Learning Resources

Using Node.js native APIs can greatly enhance the flexibility and functionality of your applications. If you're new to Node.js, the following tutorials may be helpful:

* MDN's Node.js beginner tutorial: <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction>
* Traversy Media's "Node.js Tutorial for Beginners": <https://www.youtube.com/watch?v=TlB_eWDSMt4>
* freeCodeCamp's "Node.js Basics Tutorial | Learn the Basics of Node.js in 30 Minutes": <https://www.youtube.com/watch?v=w-7RQ46RgxU>
* The Net Ninja's "Node.js Tutorial for Beginners": <https://www.youtube.com/watch?v=w-7RQ46RgxU>

These videos can help you get started with Node.js development and learn the basics and practical tips of Node.js.

[PreviousIssue Network Requests](/plugin-api/tutorial/network-request)[NextUsing Third-Party Modules](/plugin-api/tutorial/3rd-modules)

Last updated 1 year ago