---
id: 22ffy
title: Style Guide
file_version: 1.1.2
app_version: 1.3.8
---

### What is this?

To be able to maintain a consistent design and experience of the app, this _Style Guide_ will set the ground rules for both **_developing new_** components as well as **_using existing_** components.

The first part of this document is the style guide of the app, the general guidelines for designing new components and patterns in a way that ensures a cohesive visual design.

The second part of this document consists of two libraries, the component library and the pattern library. The component library showcases all available components, in all states and variations. The pattern library showcases all available patterns.

* * *

## Index

**Style guide**

*   Colours
    
*   Typography
    
*   Grid
    
*   Icons
    
*   Components
    

**Libraries**

*   Component Library
    
*   Pattern Library
    

* * *

## Colours

Base colours are named as follows:

*   Extra Extra dark
    
*   Extra dark
    
*   Dark
    
*   Light
    
*   Extra light
    
*   Extra extra light

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2F93b178b6-1775-4093-a208-835df9b1d719.png?alt=media&token=2a49f35b-69d7-4a6f-a05d-e0d1ef3f4f46" style="width:'100%'"/></div>

<br/>

* * *

## Typography

* * *

## Grid

The layout of the app is structured through the use of grids. Grids are divided into five window-size breakpoints:

Extra small - screen widths below 600px

Small - screen widths below 768px

Medium - screen widths below 992px

Large - screen widths below 1200px

Extra large - Screen widths from 1200px and above

### Extra small

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2F3192fb5b-2750-43c2-8ff7-61cb8138d60c.png?alt=media&token=1a977799-0323-4f25-ab4c-57914ec19a95" style="width:'25%'"/></div>

<br/>

### Small

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2Fc83fc305-b3da-41a7-89c3-42473ed21450.png?alt=media&token=bd89ea16-c821-4d65-961c-d56bb917c792" style="width:'50%'"/></div>

<br/>

### Medium

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2F0f414526-e732-4901-9823-4b76d3e5a006.png?alt=media&token=4cc4dc65-9840-426c-a592-c802263305de" style="width:'100%'"/></div>

<br/>

### Large

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2F3ed2be1d-bfae-4d1d-a688-ff571e35691c.png?alt=media&token=c474097b-67fa-4d49-b865-57a8760608fd" style="width:'100%'"/></div>

<br/>

### Extra large

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2F5b8290b2-75fe-410f-ac1f-c5f1481a3d92.png?alt=media&token=2a6978df-5e65-4fe5-af08-c31aa36c4364" style="width:'100%'"/></div>

<br/>

* * *

## Icons

* * *

## Components and patterns

Components should follow these sets of rules to comply with the style guide.

### Colours

The different colours in the colour palette are used to signal different things. These are guidelines, not rules.

#### **Dark and light mode**

In light mode, the _extra extra light_ colour is used as the main background colour for the _body_ element. It might also be used on elements that are behind the frontmost element, if this makes graphically sense.

In dark mode, the _extra dark_ colour is used as the main background colour for the body element, with lighter tones is used on elements further in front.

**Primary Colours**

*   **Attention** should be used to draw the users attention to an action, therefore should be mainly used on call to action elements such as buttons and anchors.
    
*   **Concentrate** should be used to mark sections of interest or focus. Use this as background colour for sections with significant content, or as an accent colour for focused elements such as text inputs.
    
*   **Regard** is used to draw the users attention to warnings or important notifications.
    

**Secondary Colours**

*   **Chosen** should be used to indicate a selected element or a chosen action.
    
*   **Remember** should be used to remind the user of upcoming events or of notifications of lesser importance.
    
*   **Recall** should be used to indicate that an action is needed. This might be a missing input, missing date or time etc.
    

### Size

**Height**

The height of elements depends on its content, padding and margins. It is desirable to follow the 4px rule (any size is divisible by 4).

<br/>

**Padding and margins**

### Drop shadows

Drop shadows should be used to signify a hierarchy of elements or whether or not an element is active. Text fields and areas will for example only have a drop shadow when focused. Drop down menus also have a drop shadow, elevating the menu element to the top of the hierarchy.

A drop shadow is subtle and relatively large. It is only offset in y-direction. It is highly blurred to give the illusion of a soft lighted environment.

> Drop shadows has these settings: x-offset = 0, y-offset = 10px, colour: extra extra dark gray, 16% opacity, blur: 26.

### Corner radius

* * *

## Component library

### Buttons

\-- **Light**

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2Fc7b29a91-d516-4a48-99a6-95772291e3d2.png?alt=media&token=77496eb0-c2a8-4a8c-9dd1-8d7e079ab339" style="width:'100%'"/></div>

<br/>

### Dropdowns

\-- **Light**

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2Fdd98293a-20bd-41f5-a82b-141847b4c529.png?alt=media&token=8e4e9c95-19e3-4b0f-b455-3e0ce3eaa750" style="width:'100%'"/></div>

<br/>

### Text Fields

\-- **Light**

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc%3D%2Fad531966-4915-4ba1-93d4-619df7b08116.png?alt=media&token=4eaf1468-7371-4311-b2ed-1fbddf6d53c7" style="width:'100%'"/></div>

<br/>

* * *

## Pattern library

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://app.swimm.io/repos/Z2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc=/docs/22ffy).
