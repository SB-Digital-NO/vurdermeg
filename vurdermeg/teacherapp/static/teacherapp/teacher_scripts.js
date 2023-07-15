/*
funksjoner:
    åpne gruppevalg-panel
    fylle inn valgte grupper i gruppe-input
    utvide legg til panel
    legge til fylt inn spørsmål i DOM
    fylle inn i skjult form (question) for hvert utfylte spørsmål
    fylle inn i skjult form (assessment) for hele vurderingen
    linke "Send inn"-knapp til submit form
    fylle inn skjult input for question formset

klasser:

*/

// ---=== new assessment ===---
let groupSelector = document.getElementById("groupSelector");
let selectWindow = document.getElementById("js_selectWindow");
let groupSelectorMarker = document.getElementById("groupSelectMarker");
let addQuestionButton = document.getElementById("id_addQuestion");
let choseQuestionDiv = document.getElementById("id_choseQuestionDiv")

var selectedGroups = [];

function openGroupSelector() {
    if (selectWindow.style.display == "none") {
        selectWindow.style.display = "grid";
        groupSelectorMarker.classList.add("selection-thumb__marker--turned")

    }
    else {
        selectWindow.style.display = "none"
        groupSelectorMarker.classList.remove("selection-thumb__marker--turned")
    }
}

function addOrRemoveGroupToSelection(group) {
    if (selectedGroups.includes(group)) {
        let gIndex = selectedGroups.indexOf(group)
        selectedGroups.splice(gIndex, 1) // removes the group from selected groups
    }
    else {
        selectedGroups.push(group)
    }
}

groupSelector.addEventListener("click", openGroupSelector);
addQuestionButton.addEventListener("click", function () {
    if (choseQuestionDiv.style.display == "none") {
        choseQuestionDiv.style.display = "block"
    }
});

let groupNodeList = document.getElementsByClassName("selection__item");

for (let i = 0; i < groupNodeList.length; i++) {
    let element = groupNodeList[i];
    element.addEventListener("click", function () {
        let gName = element.id.replace("id_", "").replace("_item", "");
        addOrRemoveGroupToSelection(gName);
    })
}

