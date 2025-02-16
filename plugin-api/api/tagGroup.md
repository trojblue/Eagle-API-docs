* [Methods](#z1a5y)
* [get()](#x9nu2)
* [create(options)](#x9nu2-1)
* [save()](#x9nu2-2)
* [remove()](#x9nu2-3)

1. [API Reference](/plugin-api/api)
# tagGroup

The eagle.tagGroup API allows easy access to the tag groups in the current application.

Copy
```
// Get all tag groups
const tagGroups = (await eagle.tagGroup.get());
```
## Methods

## get()

Retrieves all tag groups.

* Returns `Promise<tagGroups: Object[]>` - the query result for tagGroups.

Copy
```
const tagGroups = (await eagle.tagGroup.get());
```
## create(options)

Creates a new tag group.

* Returns `Promise<tagGroup: Object>` - the newly created tag group.

Copy
```
await eagle.tagGroup.create({
    name: "new group",
    color: "red",
    tags: ["tag1", "tag2"]
});
```

---

**Instance Methods**

## save()

Saves changes to the tag group.

* Returns `Promise<tagGroup: Object>` - the result of the save operation.

Copy
```
const tagGroups = (await eagle.tagGroup.get());
const tagGroup = tagGroups[0];
tagGroup.name = "new name";
tagGroup.color = "red"; // red, orange, yellow, green, aqua, blue, purple, pink
tagGroup.tags = ["tag1", "tag2"];
await tagGroup.save();
```
## remove()

Removes the tag group.

* Returns `Promise<result: boolean>` - whether the removal was successful.

Copy
```
const tagGroups = (await eagle.tagGroup.get());
const tagGroup = tagGroups[0];
await tagGroup.remove();
```
[Previoustag](/plugin-api/api/tag)[Nextlibrary](/plugin-api/api/library)

Last updated 8 days ago