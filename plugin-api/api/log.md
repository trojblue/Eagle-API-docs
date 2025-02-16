* [debug(obj)](#haugb)
* [info(obj)](#qxf3f)
* [warn(obj)](#ctpju)
* [error(obj)](#mo6j1)

1. [API Reference](/plugin-api/api)
# log

Log specific information in Eagle software for debugging and troubleshooting during development.

Click here to see how to obtain Eagle [software logs](https://docs-cn.eagle.cool/article/92-how-do-i-get-the-error-log).

Copy
```
eagle.log.debug('debug message from plugin');
eagle.log.info('info message from plugin');
eagle.log.warn('warn message from plugin');
eagle.log.error('error message from plugin');
// [13:19:39.845] [debug] [plugin] "debug message from plugin"
// [13:19:39.845] [info] [plugin] "info message from plugin"
// [13:19:39.845] [warn] [plugin] "warn message from plugin"
// [13:19:39.845] [error] [plugin] "error message from plugin"
```

---

#### Methods

## debug(obj)

Log debug-type content to the software log

* `obj` Object - The content to be recorded, can be `Object`, `String`, `Array`, and other formats

Copy
```
eagle.log.debug(obj);
eagle.log.debug(array);
eagle.log.debug('error message from plugin');
```

---

## info(obj)

Log info-type content to the software log

* `obj` Object - The content to be recorded, can be `Object`, `String`, `Array`, and other formats

---

## warn(obj)

Log warn-type content to the software log

* `obj` Object - The content to be recorded, can be `Object`, `String`, `Array`, and other formats

---

## error(obj)

Log error-type content to the software log

* `obj` Object - The content to be recorded, can be `Object`, `String`, `Array`, and other formats

Copy
```
try {
    let a = {};
    a.b.c = 'test';
}
catch (err) {
    eagle.log.error('error message from plugin');
    eagle.log.error(err.stack || err);
}
// [13:23:24.191] [error] [plugin] "error message from plugin"
// [13:23:24.191] [error] [plugin] "TypeError: Cannot set properties of undefined (setting 'c')\n    at <anonymous>:3:11"
```

---

[Previousshell](/plugin-api/api/shell)[NextFFmpeg](/plugin-api/extra-module/ffmpeg)

Last updated 1 year ago