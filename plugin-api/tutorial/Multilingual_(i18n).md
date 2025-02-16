* [Step 1: Create the \_locales folder](#step-1-create-the-_locales-folder)
* [Step 2: Create language .json files](#step-2-create-language-.json-files)
* [Step 3: Adjust manifest.json](#step-3-adjust-manifest.json)
* [Step 4: Replace strings used in the code](#step-4-replace-strings-used-in-the-code)
* [Step 5: Switch application language and check the modification results](#step-5-switch-application-language-and-check-the-modification-results)
* [Learn Advanced Usage](#learn-advanced-usage)

1. [Developer Guide](/plugin-api/tutorial)
# Multilingual (i18n)

The Eagle plugin comes with a built-in i18next module, allowing developers to easily create multilingual plugins. i18next is a JavaScript internationalization library that makes translation and locali

[PreviousUsing Third-Party Modules](/plugin-api/tutorial/3rd-modules)[NextFrameless Window](/plugin-api/tutorial/frameless-window)

Last updated 7 months ago

The Eagle plugin has a built-in i18next module, making it easy for developers to create plugins that support multiple languages. i18next is a JavaScript library for multilingual applications, which can easily handle multilingual translations, and provides support for various translation methods, including custom translations, localization, and multi-language support.

Below we will walk you through how to make your plugin support multiple languages:

## Step 1: Create the `_locales` folder

## Step 2: Create language `.json` files

\_locales/en.json\_locales/zh\_CN.json\_locales/zh\_TW.json\_locales/ja\_JP.jsonCopy
```
{
    "manifest": {
        "app": {
            "name": "i18n example"
        }
    },
    "contextMenu": {
        "copy": "Copy",
        "paste": "Paste"
    }
}
```
Copy
```
{
    "manifest": {
        "app": {
            "name": "Multilingual example"
        }
    },
    "contextMenu": {
        "copy": "复制",
        "paste": "粘贴"
    }
}
```
Copy
```
{
    "manifest": {
        "app": {
            "name": "Multilingual example"
        }
    },
    "contextMenu": {
        "copy": "複製",
        "paste": "貼上"
    }
}
```
Copy
```
{
    "manifest": {
        "app": {
            "name": "i18n の例"
        }
    },
    "contextMenu": {
        "copy": "コピー",
        "paste": "ペース"
    }
}
```

Currently supported languages are `en`, `ja_JP`, `es_ES`, `de_DE`, `zh_TW`, `zh_CN`, `ko_KR`, `ru_RU`.

## Step 3: Adjust `manifest.json`

Using Eagle Plugin's `i18next` feature, you can define translations for multilingual applications with simple JSON files.

Copy
```
{
    "id": "LE564883T24ZR",
    "version": "1.0.0",

    // 1. Adjust the name
    "name": "{{manifest.app.name}}",
    "logo": "/logo.png",
    "keywords": [],

    // 2. Set supported languages and default language
    "fallbackLanguage": "zh_CN",
    "languages": ["en", "zh_TW", "zh_CN", "ja_JP"],

    "main": {
        "url": "index.html",
        "width": 640,
        "height": 480
    }
}
```
## Step 4: Replace strings used in the code

Adjust plugin.js, use i18next method to get strings and perform alert

plugin.jsCopy
```
eagle.onPluginCreate((plugin) => {
    // Get multilingual fields
    let copyText = i18next.t('contextMenu.copy');
    let pasteText = i18next.t('contextMenu.paste');
    document.querySelector('#message').innerHTML = `
    <ul>
        <li>Language: ${eagle.app.locale}</li>
        <li>Copy: ${copyText}</li>
        <li>Paste: ${pasteText}</li>
    </ul>
    `;
});
```
## Step 5: Switch application language and check the modification results

You can change the language settings of Eagle software by following these steps: Find and click the "Eagle" button on the screen, then select "Preferences", click "Common", and finally modify the "Language" section.

**Complete Example Code:**

<https://github.com/eagle-app/eagle-plugin-examples/tree/main/i18n>

## Learn Advanced Usage

i18next has many convenient methods that allow us to easily cope with various translation scenarios. To ensure brevity, only the core usage methods are explained here. If you need to learn more about i18next usage and advanced techniques, it's recommended to read the following links:

* i18next Official Documentation: <https://www.i18next.com/overview/getting-started>
* i18next GitHub Repository: <https://github.com/i18next/i18next>

By reading the official documentation, you can understand the basic concepts and usage of i18next and find some example code to help you get started using it. The GitHub repository contains the source code and more documentation of i18next. If you want to further understand its implementation details, you can check it out there.

Switch application language

![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252Fgit-blob-569807c86a1c45f8575718fb2d6ba12d5de015c9%252Fimage%2520%2819%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=7ac83908&sv=2)![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252FBUvYim43D84nY7NnPlBI%252Fimage.png%3Falt%3Dmedia%26token%3D3d752173-a1c1-45cd-b17d-e7843f1fee71&width=768&dpr=4&quality=100&sign=852313f5&sv=2)![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252Fd8A9rC3ZEsX62e1XDE3v%252Fimage.png%3Falt%3Dmedia%26token%3D4637cc4a-4546-4fd9-a1d4-2c184a71fe75&width=768&dpr=4&quality=100&sign=3e2c9688&sv=2)![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252Fgit-blob-a32e2c55e65473ae04516b88f980c83fc620a3ba%252Fimage%2520%2820%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=31634b10&sv=2)![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252Fgit-blob-cb19a0370eaf4f0da654e55033aeda93aa49c713%252Fimage%2520%2816%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=9a1eb604&sv=2)