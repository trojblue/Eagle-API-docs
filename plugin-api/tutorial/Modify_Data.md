* [Example 1: Modify the selected file of the current application](#example-1-modify-the-selected-file-of-the-current-application)
* [Example 2: Modify folder properties](#example-2-modify-folder-properties)

1. [Developer Guide](/plugin-api/tutorial)
# Modify Data

You can directly modify the results obtained using the Eagle Plugin API method. To save the modified results, just call the `save()` method of the result object. Here are some simple examples:

## **Example 1: Modify the selected file of the current application**

Copy
```
// Get the currently selected file in the Eagle app
let items = await eagle.item.getSelected();
let item = items[0];
// Modify tags
item.tags = ['tag1', 'tag2'];
// Save changes
await item.save();

```
## **Example 2: Modify folder properties**

Copy
```
// Get the currently selected folder in the Eagle app
let folder = (await eagle.folder.getSelected())[0];
// Modify properties
folder.name = 'New Folder Name';
folder.description = 'New description...';
// Save changes
await folder.save();
```

**🦄 Best Practice:** To ensure data security, use the API-provided `save()` method for data access and modification, and avoid directly modifying any files under the Eagle resource library.

[PreviousRetrieve Data](/plugin-api/tutorial/get-eagle-data)[NextAccess Local Files](/plugin-api/tutorial/access-local-files)

Last updated 1 year ago