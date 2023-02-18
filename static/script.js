// var myButton = document.getElementById("create-vocablist-btn");
// myButton.addEventListener("click", function() {
//     window.location.href = "/create-vocablist";
// });

function changeText() {
    document.getElementById("create-vocablist-btn").innerHTML = "VocabList Created!";
}

function goToVocabListWindow() {
    window.location.href = "/create-vocablist";
}