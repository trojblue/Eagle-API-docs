* [Glossary](#id-1-product-policies)
* [1. Plugin Policies](#id-1-product-policies-1)
* [1.1 Unique Functionality and Value; Accurate Representation](#id-1.1-unique-functionality-and-value-accurate-representation)
* [1.2 Plugins must be testable](#id-1.2-plugins-must-be-testable)
* [1.3 Functionality Availability](#id-1.3-functionality-availability)
* [1.4 Advertising Behavior](#id-1.4-a-dvertising-behavior)
* [2. Security Policies](#id-2.-security-policies)
* [2.1 Information Security](#id-2.1-information-security)
* [2.2 Privacy and Personal Information](#id-2.2-privacy-and-personal-information)
* [3. Financial Transactions](#id-3.-financial-transactions)
* [3.1 Payment Functionality](#id-3.1-payment-functionality)
* [3.2 Disclosure of Payment Functionality](#id-3.2-disclosure-of-payment-functionality)
* [4. Content Policies](#id-4.-content-policies)
* [4.1 Content Requirements for Eagle Plugin Center Listings](#id-4.1-content-requirements-for-eagle-plugin-center-listings)
* [4.2 Content Includes Names, Icons, Original and Third-Party](#id-4.2-content-includes-names-icons-original-and-third-party)
* [4.3 Risk of Harm](#id-4.3-risk-of-harm)
* [4.4 Prohibited Content, Inappropriate Content, Activities, and Services](#id-4.4-prohibited-content-inappropriate-content-activities-and-services)

1. [Distribution](/plugin-api/distribution)
# Developer Policies

This article aims to help you understand our developer policies and related specifications.

We may update our policy terms from time to time, so please refer to the policy terms at that time.

Thank you for participating in the development of Eagle plugins. Your contribution is extremely important to our community. Before you start the development process, we hope you can take some time to read and comply with the following developer policies. These policies are designed to ensure that every user's experience is of the highest quality and that all plugins meet our standards and expectations.

Thank you again for your participation and we look forward to seeing your innovative results.

## Glossary

1. Eagle: Also known as [Eagle App](https://en.eagle.cool/), a professional tool for image collection and management.
2. Eagle plugin: Also known as "Eagle extension plugin, plugin, Eagle Plugin, Plugin", refers to the name of the process you developed based on the Eagle Plugin API.
3. Eagle Plugin Center: The affiliated function of [Eagle Community](https://community-en.eagle.cool), where you can share the plugins you developed with others.
4. macOS: A product trademark belonging to [Apple](https://apple.com/), an operating system developed and maintained by Apple.
5. Windows: A product trademark belonging to [Microsoft](https://microsoft.com/), an operating system developed and maintained by Microsoft.

---

## 1. Plugin Policies

### 1.1 Unique Functionality and Value; Accurate Representation

Eagle plugins and related relay data must accurately and clearly describe their source and functionality.

**1.1.1 Extension plugins must have a single purpose**

Eagle plugins must have a clear and specific single-purpose function.

**1.1.2 Describe your Eagle plugin**

Eagle plugins must accurately and clearly describe the functions you have developed and any important limitations, including necessary or supported input devices. During the first run experience, your Eagle plugin must clearly indicate its own functions or limitations.
Eagle plugins may not use names or icons similar or similar to existing Eagle plugins, and if you do not have permission, you may not claim to represent a company, government agency, or other entity.

**1.1.3 Functionality and Operation**

The Eagle plugin functionality you develop must operate completely normally.

**1.1.4 Search and Exploration**

Your "plugin keywords" search terms should not exceed six single words and should be related to your plugin.

**1.1.5 Stability and Performance**

Your plugin functionality should not have a negative impact on the performance or stability of Eagle or the system.

**1.1.6 Process Code Obfuscation**

Process code obfuscation is not allowed. This includes the process code in the Eagle plugin and any external process codes or resources retrieved from the network. If your process code cannot be reviewed, the Eagle Plugin Center may require you to modify the process code to a readable level.

**1.1.7 Change Eagle App or System Configuration**

Eagle plugins must not change the functionality or configuration of Eagle or the system without properly notifying and obtaining user consent. Any system configuration changes or adjustments should be clearly recorded in the Eagle plugin's description and require user consent before proceeding.

**1.1.8 License**

Your Eagle plugin can only request the license required for operation. You must provide a description of how the Eagle plugin works. Your Eagle plugin can only run as described. Your Eagle plugin may not require functionality licenses beyond what is required for declared operation and operation.

**1.1.9 Localization**

You should localize your Eagle plugin for all languages declared to be supported. The text of the Eagle plugin description should be localized in each language you declare.

If your Eagle plugin has been localized, and some features cannot be used in the localized version, you must clearly state or display the limitations of localization in the Eagle plugin description. The experience provided by the Eagle plugin must be similar in all supported languages.

**1.1.10 Plugin Presentation and Consistency**

We hope that the Eagle Plugin Center can maintain a consistent design aesthetic and user experience. Therefore, the plugin icons, screenshots, plugin names, and descriptions you provide should meet our "Examples" requirements. If your plugin does not meet our requirements in these areas, we reserve the right to not approve it. These requirements are designed to ensure the quality of the plugin and maintain the overall aesthetics and consistency of the Eagle Plugin Center.

### 1.2 Plugins must be testable

The submitted Eagle plugin must be testable. If for any reason your Eagle plugin cannot be tested, including but not limited to the following cases, your Eagle plugin may not meet this requirement.

**1.2.1 User Authentication**

If your Eagle plugin requires login authentication, please provide a valid demo account.

**1.2.2 Service Availability**

If your Eagle plugin requires access to a server, the server must be able to operate normally to confirm its normal operation.

### 1.3 Functionality Availability

**1.3.1 Cross-platform compatibility**

Eagle plugins should be compatible with all devices and platforms that Eagle can download (macOS & Windows).

If you download an Eagle plugin on an incompatible device, it should detect it at startup and prompt the user with a message explaining that the device must meet the requirements for Eagle plugin compatibility to operate.

**1.3.2 User Experience**

* Eagle plugins must start immediately and must maintain responsiveness to user input.
* Eagle plugins must continue to run and maintain responsiveness to user input.
* Eagle plugins must shut down normally and not shut down unexpectedly.
* Eagle plugins should handle exceptional situations and maintain responsiveness to user input after handling exceptional situations.

### 1.4 Advertising Behavior

Eagle plugins may not contain any form of advertising (including but not limited to video, animation, and text).

---

## 2. Security Policies

### 2.1 Information Security

Your Eagle plugin functionality must not compromise or harm the security or functionality of users' devices, systems, or related systems.

**2.1.1 Spam and Malware**

Your developed Eagle plugin must not contain or activate malicious process codes.

**2.1.2 Dependency on Other Software**

Your Eagle plugin may depend on non-integrated or other third-party software products (such as another product, module, or service) to provide primary functionality, provided that you must disclose the dependency in the description.

**2.1.3 Eagle Plugin Updates**

Unless otherwise permitted by Eagle, your Eagle plugin can only be updated through the Eagle Plugin Center.

### 2.2 Privacy and Personal Information

The following requirements apply to Eagle plugins that access personal information. Personal information includes all information or data that identifies or can be used to identify a person or is associated with such information or data.

**2.2.1 Collect Personal Information Only When Necessary and with User Consent**

Eagle plugins can only collect, access, use, or transmit personal information (including web activity) when users explicitly consent.

**2.2.2 Maintain Privacy Principles**

Regardless of whether your Eagle plugin accesses, collects, or transmits personal information, if required by law, you must provide important notices and comply with your privacy principles. Your privacy principles must notify users of how the Eagle plugin accesses, collects, or transmits personal information, how the information is used, stored, and protected, and the types of objects that disclose the information.

Your privacy principles must describe the use and sharing of user information, how to control access to their information, and must comply with applicable laws and regulations. When creating new features for Eagle plugins, your privacy principles must be kept up to date.

If you provide privacy principles for Eagle plugins, you agree to allow Eagle to share such privacy principles with users of Eagle plugins.

**2.2.3 Sharing Data with Collaborating Vendors**

You can only publish personal information of Eagle plugin users to external services or collaborating vendors through Eagle plugins or related relay data after obtaining the consent of these users. Consent to join means that users provide their quick permission in the Eagle plugin user interface you require activity in the following situations:

* Describe how information is accessed, used, or shared with users and indicate the type of object disclosed.
* Provide a mechanism in the Eagle plugin user interface for users to choose to revoke permission and exit later.

**2.2.4 Sharing Non-User Information**

If you publish personal information of individuals to external services or collaborating vendors through Eagle plugins or relay data, but the person sharing the information is not a user of the Eagle plugin:

2. You must obtain explicit written consent to publish the personal information.
5. You must allow the person sharing the information to revoke the consent at any time.
8. Your privacy principles must clearly disclose that you may collect personal information in this way.
11. If required by applicable law, you must delete any personal information of individuals, including those collected in this way.
14. This requirement also applies if your Eagle plugin allows users to access personal information of another person.

**2.2.5 Secure Transmission of Information**

If your Eagle plugin collects, stores, or transmits personal information, it must use reasonable and secure password compilation methods to perform this action securely.

**2.2.6 Highly Sensitive Information**

Your Eagle plugin must not collect, store, or transmit highly sensitive personal information, such as health or financial information, unless such information is related to the functionality of the Eagle plugin. Your Eagle plugin must also obtain user consent before collecting, storing, or transmitting such information.

---

## 3. Financial Transactions

If your product contains in-app purchases, subscription accounts, virtual currency, billing functions, or collects financial information, the requirements in the following sections apply.

### **3.1 Payment Functionality**

Your Eagle plugin allows users to access digital content or services by purchasing through third-party payment API platforms.

You must use a secure third-party payment API platform to purchase physical goods or services. For payments related to any other service, including physical gambling or charitable donations, you must also use a secure third-party payment API platform.

* If your Eagle plugin is used to facilitate or collect charitable donations, or conduct promotional lotteries/contests, you must comply with applicable laws.
* You must also clearly state that Eagle is not the fundraiser or sponsor of this promotion.
* Products sold in your Eagle plugin cannot be converted into any legally valid currency (such as US dollars, euros, etc.) or any physical goods or services.

The following requirements apply when using a secure third-party payment API platform:

* Your Eagle plugin must identify the commercial transaction provider, verify the user, and obtain the user's confirmation when collecting any payment or financial information from the user during the transaction. The commercial transaction provider maintains a secure platform for financial exchanges.
* Eagle plugins may provide users with the ability to save this verification, but users must be able to request verification for each transaction or turn off in-app transactions.
* If your Eagle plugin functionality collects credit card information or uses a third-party payment processor that collects credit card information, the payment processor must comply with the current PCI Data Security Standard (PCI DSS).

### **3.2 Disclosure of Payment Functionality**

Your Eagle plugin and its related metadata must provide information about the type and price range of in-app purchases. You must not mislead users and must clearly state the nature of your in-app promotions and offerings, including the scope and terms of any trial experience.

---

## 4. Content Policies

The following policies apply to content and metadata (including publisher name, extension name, extension icon, extension description, extension screenshots, extension trailers and trailer thumbnails, and any other extension metadata) distributed in the "Eagle Plugin Center". Content refers to images, sounds, videos, and copy contained in your extension, blocks, notifications, error messages, or advertisements publicly available through your extension, and any content transmitted from servers or connected to your extension.

Because extensions and the "Eagle Plugin Center" are used globally, these requirements are interpreted and applied in the context of regional and cultural norms.

### 4.1 Content Requirements for Eagle Plugin Center Listings

Your relay data and other content included with the Eagle plugin may contain incomplete or immature content. Eagle plugin submissions that do not meet Eagle standards will be rejected or immediately removed.

### 4.2 Content Includes Names, Icons, Original and Third-Party

All content in your extension and its related metadata must be original to you or appropriately licensed from third-party rights holders and can only be used in accordance with the rights holders' licenses or other legal permissions.

### 4.3 Risk of Harm

**4.3.1 Requirements**

Your extension must not contain any content that promotes or glorifies the following real-world activities:

* Extreme or gratuitous violence
* Human rights violations
* Manufacture of illegal weapons
* Use of weapons against people, animals, or real or personal property.

**4.3.2 Responsibility**

Your Eagle plugin cannot:

* Pose a security risk to end-users or any other person or animal, or cause them discomfort, injury, or any other harm
* Pose or cause a risk of damage to real or personal property. You are responsible for all security testing of extensions, certificate acquisition, and implementation of any appropriate functional protection measures.

You cannot disable any platform's security or comfort features and must include all applicable legal requirements and industry-standard warnings, notices, and disclaimers in your extension.

### 4.4 Prohibited Content, Inappropriate Content, Activities, and Services

Eagle plugins must comply with the following conditions:

* Eagle plugins must not contain any defamatory, libelous, slanderous, or threatening content.
* Eagle plugins must not contain online games, sports entertainment, gambling, or other content that provides cash or other value.
* Eagle plugins must not contain content related to cryptocurrency transactions.
* Eagle plugins must not contain content or functionality that encourages, promotes, or glorifies illegal activities in the real world.
* Eagle plugins must not contain profanity.
* Eagle plugins must not contain content that promotes alcohol, tobacco, drugs, or related content.
* Eagle plugins must not contain or display content that reasonable people would consider unreasonable.
* Eagle plugins must not contain any content that is offensive in any country/region. Due to local laws or cultural norms, content may be considered offensive in specific countries/regions.
* Eagle plugins must not contain any adult content (R18).

---

***Eagle reserves the right to make the final review.***

Policy last updated: *2023-11-01 11:11*

[PreviousUpdate Plugin](/plugin-api/distribution/update)[Nextmanifest.json Configuration](/plugin-api/tutorial/manifest)

Last updated 1 year ago