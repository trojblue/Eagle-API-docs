* [Methods](#z1a5y)
* [open(menuItems)](#tkp0d)

1. [API Reference](/plugin-api/api)
# contextMenu

Create native application context menus.

## Methods

## open(menuItems)

Pops up the right-click menu.

* `menuItems` : [MenuItem](https://www.electronjs.org/docs/latest/api/menu-item)

  + `id` string - Menu item ID
  + `label` string - Text displayed for the menu item
  + `submenu` [MenuItem] - Submenu

Copy
```
eagle.contextMenu.open([
    {
        id: "edit",
        label: "Edit",
        submenu: [
            {
                id: "resize",
                label: "Resize",
                click: () => { alert("Image resized") }
            },
            {
                id: "crop",
                label: "Crop",
                click: () => { alert("Image cropped") }
            },
            {
                id: "rotate",
                label: "Rotate",
                click: () => { alert("Image rotated") }
            }
        ]
    },
    {
        id: "effects",
        label: "Effects",
        submenu: [
            {
                id: "grayscale",
                label: "Grayscale",
                click: () => { alert("Grayscale effect applied") }
            },
            {
                id: "sepia",
                label: "Sepia",
                click: () => { alert("Sepia effect applied") }
            },
            {
                id: "invert",
                label: "Invert Colors",
                click: () => { alert("Color inversion applied") }
            }
        ]
    },
    {
        id: "export",
        label: "Export",
        click: () => { alert("Image exported") }
    }
])
```
[Previousnotification](/plugin-api/api/notification)[Nextdialog](/plugin-api/api/dialog)

Last updated 9 months ago