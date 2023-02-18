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

function addTerm() {
    var container = document.getElementById("terms-container");
    var count = container.childElementCount + 1;
  
    var termGroup = document.createElement("div");
    termGroup.className = "term-group";
    var label = document.createElement("label");
    label.setAttribute("for", "term" + count);
    label.className = "form-label";
    label.innerHTML = "Term " + count + ":";
    var input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("name", "term" + count);
    input.setAttribute("id", "term" + count);
    input.setAttribute("placeholder", "Enter term...");
    input.className = "form-input";
    input.required = true;
  
    termGroup.appendChild(label);
    termGroup.appendChild(input);
  
    container.appendChild(termGroup);
}

function handleSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const formDataJSON = JSON.stringify(Object.fromEntries(formData));


    fetch('/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: formDataJSON
      })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          // Redirect to home.html
          window.location.href = '/create';
        })
        .catch(error => console.error(error));


    //window.location.href = "/submittedlist";
    
    
  }