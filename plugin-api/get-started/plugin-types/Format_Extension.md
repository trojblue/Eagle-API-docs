1. [Getting Started](/plugin-api/get-started)
3. [Plugin Types](/plugin-api/get-started/plugin-types)
# Format Extension

This article will illustrate the basic concepts of format extension plugins.

The main purpose of format extension plugins is to enable Eagle to preview file formats that are not yet supported. Unlike other types of plugins, format extension plugins do not need to define the `main` attribute in `manifest.json`, but need to set the `preview` attribute. Here is an example code:

Copy
```
"preview": {}
```

In the `preview`, you can define the file extensions you want to extend. For example, if you want Eagle to support the icns icon format, you can enter `"icns": {}`:

Copy
```
"preview" : {
    "icns": {}
}
```

If you need to set multiple extensions, you can use a comma `,` to separate different extensions for definition, for example:

Copy
```
"preview" : {
    "icns,ico": {}
}
```

Format extension plugins can be divided into two parts:

1. `"thumbnail.path"`: Provides the `.js` file for parsing the thumbnail of the file format to be extended.
2. `"viewer.path"`: Provides the `.html` file for previewing the format to be extended.

Copy
```
"preview": {
    "icns": {
        "thumbnail": {
            "path": "thumbnail/icns.js",
            "size": 400,
            "allowZoom": false
        },
        "viewer": {
            "path": "viewer/icns.html"
        }
    }
}
```

After setting other `metadata.json` fields, the final code is as follows:

manifest.jsonthumbnail/icns.jsviewer/icns.htmlCopy
```
{
    "id": "LARSKLB8OTOC2",
    "version": "1.0.0",
    "platform": "all",
    "arch": "all",
    "name": "Preview Plugin",
    "logo": "/logo.png",
    "keywords": [
        "icns"
    ],
    "devTools": false,
    "preview": {
        "icns": {
            "thumbnail": {
                "path": "thumbnail/icns.js",
                "size": 400,
                "allowZoom": false
            },
            "viewer": {
                "path": "viewer/icns.html"
            }
        }
    }
}
```
Copy
```
const fs = require('fs');
const icns = require('./../js/icns-util.js');
const imageSize = require('./../js/image-size.js');
module.exports = async ({ src, dest, item }) => {
    return new Promise(async (resolve, reject) => {
        try {
            // 1. parsing and generate thumbnail file to dest
            await icns.icns2png(src, dest);
            let size = await imageSize(dest);
            // 2. Check if the result is correct
            if (!fs.existsSync(dest) || size.width === 0) {
                return reject(new Error(`icns file thumbnail generate fail.`));
            }
            // 3. update the item dimensions
            item.height = size?.height || item.height;
            item.width = size?.width || item.width;
            // 4. return the result
            return resolve(item);
        }
        catch (err) {
            return reject(err);
        }
    });
}
```
Copy
```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ICNS Viewer</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        #viewer {
            pointer-events: none;
            object-fit: contain;
            object-position: center;
            width: 100%;
            height: 100%;
            max-width: 100vw;
            max-height: 100vh;
        }
    </style>
</head>
<body>
    <img id="viewer"/>
    <script>
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('id');
        const filePath = urlParams.get('path');
        const width = urlParams.get('width');
        const height = urlParams.get('height');
        const theme = urlParams.get('theme');
        const lang = urlParams.get('lang');
        const viewer = document.querySelector('#viewer');
        // 1. Load the thumbnail image first
        // 👍 Avoid loading for too long, and UI has no content
        viewer.src = filePath.replace(".icns", "_thumbnail.png");
        // 2. Load the file and replace thumbnail
        (async function() {
            const icns = require('./../js/icns-util.js');
            let buffer = await icns.icns2buffer(filePath);
            let base64 = `data:image/png;base64,${buffer.toString('base64')}`;
            viewer.src = base64;
        })();
    </script>
</body>
</html>
```

Please note that currently the format extension plugins do not support Eagle Plugin API and DevTools debugging functionality.

**Complete Example Code:**
<https://github.com/eagle-app/eagle-plugin-examples/tree/main/Preview>

[PreviousBackground Service](/plugin-api/get-started/plugin-types/service)[NextInspector](/plugin-api/get-started/plugin-types/inspector)

Last updated 10 months ago