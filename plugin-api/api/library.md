* [Methods](#z1a5y)
* [info()](#s7pkf)
* [Properties](#adtwq)
* [name string](#qxggi)
* [path string](#qxggi-1)
* [modificationTime Integer](#modificationtime-integer)

1. [API Reference](/plugin-api/api)
# library

Get information about the repository currently being used by Eagle.

## Methods

## info()

Get detailed information about the current repository, including folders, smart folders, tag groups, etc.

* Returns `Promise<data: Object>`

  + `data` Object - Various properties of the repository

Copy
```
console.log(await eagle.library.info());
```

---

## Properties

The `library` module includes the following properties:

## `name` string

Returns the name of the current repository

Copy
```
console.log(eagle.library.name)
// test
```
## `path` string

Returns the path where the current repository is located

Copy
```
console.log(eagle.library.path);
// C:\Users\User\Pictures\Design.library
```
## `modificationTime` Integer

Returns the last modification time (timestamp)

Copy
```
console.log(eagle.library.modificationTime);
// 1681281134495
```
[PrevioustagGroup](/plugin-api/api/tag-group)[Nextwindow](/plugin-api/api/window)

Last updated 1 year ago