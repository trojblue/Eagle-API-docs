* [Example 1: Get the currently selected file in the application](#example-1-get-the-currently-selected-file-in-the-application)
* [Example 2: Get files by specified conditions](#example-2-get-files-by-specified-conditions)
* [Example 3: Get the currently selected folder in the application](#example-3-get-the-currently-selected-folder-in-the-application)

1. [Developer Guide](/plugin-api/tutorial)
# Retrieve Data

You can access various data stored in the Eagle application through methods provided by the Eagle Plugin API, such as `files`, `folders`, `libraries`, etc. Here are some simple examples:

## **Example 1: Get the currently selected file in the application**

Copy
```
let selected = await eagle.item.getSelected();
console.log(selected);
```
## **Example 2: Get files by specified conditions**

Copy
```
let items = await eagle.item.get({
    ids: [],
    isSelected: true,
    isUnfiled: true,
    isUntagged: true,
    keywords: [""],
    ext: "",
    tags: [],
    folders: [],
    shape: "square",
    rating: 5,
    annotation: "",
    url: ""
});
```
## **Example 3: Get the currently selected folder in the application**

Copy
```
let folders = await eagle.folder.getSelected();
```

In addition to the above, the Eagle Plugin API provides many different APIs for getting information. Please click the link below to view the complete information:

* [Library](/plugin-api/api/library)
* [Item](/plugin-api/api/item)
* [Folder](/plugin-api/api/folder)
* [App](/plugin-api/api/app)
* [Operating System](/plugin-api/api/os)
* [Notification](/plugin-api/api/notification)
* [Dialog](/plugin-api/api/dialog)
* [Clipboard](/plugin-api/api/clipboard)
* [Log](/plugin-api/api/log)

[Previousmanifest.json Configuration](/plugin-api/tutorial/manifest)[NextModify Data](/plugin-api/tutorial/modify-eagle-data)

Last updated 1 year ago