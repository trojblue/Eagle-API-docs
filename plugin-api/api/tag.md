* [Methods](#z1a5y)
* [get()](#x9nu2)
* [getRecents()](#dwsxw)

1. [API Reference](/plugin-api/api)
# tag

The eagle.tag API allows easy access to the tags in the current application.

Copy
```
// Get all tags
const tags = (await eagle.tag.get());
// Get recently used tags
const recents = (await eagle.tag.getRecents());
```
## Methods

## get()

Retrieves all tags.

* Returns `Promise<tags: Object[]>` - the query result for tags.

Copy
```
const tags = (await eagle.tag.get());
```

---

## getRecents()

Retrieves the most recently used tags.

* Returns `Promise<tags: Object[]>` - the query result for tags.

Copy
```
const recents = (await eagle.tag.getRecents());
```
[Previousfolder](/plugin-api/api/folder)[NexttagGroup](/plugin-api/api/tag-group)

Last updated 10 months ago