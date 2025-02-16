* [Using the Third-Party Module is.js](#using-the-third-party-module-is.js)
* [Third-Party Package Management Tool: NPM](#zql65)

1. [Developer Guide](/plugin-api/tutorial)
# Using Third-Party Modules

In addition to Node.js's native APIs, you can also use third-party modules in your plugin code. These third-party modules for Node.js are created and maintained by community developers, offering a var

## Using the Third-Party Module is.js

Using third-party modules is similar to using native modules; you simply need to import them using the `require()` function.

Taking `is.js` as an example, it is a data type checking library for JavaScript. It provides a set of methods to determine if a variable's data type meets expectations.

First, you need to install the `is.js` module in Node.js using the following command:

Copy
```
npm install is_js --save
```

Note: The npm package name for is.js is is\_js, with an underscore in the name.

After installation, you can use the `is.js` module in your Node.js application process. For example, you can import the `is.js` module and use its functions like this:

Copy
```
const is = require('is_js');
if (is.number(x)) {
  console.log('x is a number');
}
else {
  console.log('x is not a number');
}
```

With the `is.js` library, you can easily perform type checks on variables in JavaScript, avoiding errors caused by type mismatches.

If you want to integrate it into the Eagle plugin, here is an example code and its execution result:

Copy
```
const is = require('is_js');
eagle.onPluginCreate(() => {
    var x = 1;
    if (is.number(x)) {
        document.write('x is a number');
    } else {
        document.write('x is not a number');
    }
});
```

The example project above can be obtained [here](https://github.com/eagle-app/eagle-plugin-examples/tree/main/3rd-party)

---

## Third-Party Package Management Tool: NPM

npm is the official package management tool for Node.js that provides a convenient way to manage third-party modules and publish your own modules. With npm, you can quickly install modules using the `npm install` command. npm offers powerful module management features to help you better manage project dependencies and module versions, improving development efficiency.

Additionally, npm provides an online module repository where you can search and download third-party modules. Overall, npm is an indispensable tool for Node.js developers, offering a range of practical features to help you better develop and manage your projects.

**npm Official Website -** <https://www.npmjs.com/>

[PreviousUsing Node.js Native API](/plugin-api/tutorial/node-js-native-api)[NextMultilingual (i18n)](/plugin-api/tutorial/i18n)

Last updated 1 year ago

Execution result

![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252F4opQcFHB7oNAnejI0WOQ%252Fimage.png%3Falt%3Dmedia%26token%3Da032876f-2a0c-4c8f-83c6-455e6a1686b8&width=768&dpr=4&quality=100&sign=442d2a21&sv=2)