* [Methods](#z1a5y)
* [tmpdir()](#a6hjz)
* [version()](#gxw5i)
* [type()](#jauoc)
* [release()](#jmfqv)
* [hostname()](#w5b2t)
* [homedir()](#iiwv7)
* [arch()](#eekcv)

1. [API Reference](/plugin-api/api)
# os

Similar to the os module in Node.js, provides some basic system operation functions.

## Methods

## tmpdir()

Get the default temporary file path of the operating system.

* Returns `string` - The default temporary file path of the operating system

Copy
```
eagle.os.tmpdir();         // 'C:\\Users\\User\\AppData\\Local\\Temp'
```

---

## version()

Get the string of the operating system kernel version.

* Returns `string` - The string of the operating system kernel version

Copy
```
eagle.os.version();         // 'Windows 10 Home'
```

---

## type()

Returns the name of the operating system.
For example: returns `Darwin` on macOS, and `Windows_NT` on Windows.

* Returns `string` - The name of the operating system

Copy
```
eagle.os.type();         // 'Windows_NT', 'Darwin'
```

---

## release()

Returns the release version of the operating system.

* Returns `string` - The release version of the operating system

Copy
```
eagle.os.release();         // '10.0.22621'
```

---

## hostname()

Returns the hostname of the operating system.

* Returns `string` - The hostname of the operating system

Copy
```
eagle.os.hostname();         // 'My_Windows'
```

---

## homedir()

Returns the home directory of the current user.

* Returns `string` - The home directory of the current user

Copy
```
eagle.os.homedir();         // 'C:\\Users\\User'
```

---

## arch()

Returns the CPU architecture of the operating system.

* Returns `string` - The current CPU architecture

  + `x64`
  + `arm64`
  + `x86`

Copy
```
eagle.os.arch();         // 'x64'
```
###

[Previousapp](/plugin-api/api/app)[Nextscreen](/plugin-api/api/screen)

Last updated 1 year ago