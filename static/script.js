function changeText() {
    document.getElementById("create-vocablist-btn").innerHTML = "VocabList Created!";
}

function goToVocabListWindow() {
    window.location.href = "/create-vocablist";
}

function goToDonatePage() {
    window.location.href = "/donate";
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
    window.location.href = "/";
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
          window.location.href = '/';
        })
        .catch(error => console.error(error));
    
  }

  function handleDonate(event) {
    window.location.href = "/";
    event.preventDefault();
    //window.location.href = "/";
    let name = document.getElementById("name").value;
    let quantity = document.getElementById("quantity").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;
    payload = {
        "amount": quantity,
        "description": message,
        "name": name,
        "recipient": email
    }
    console.log(payload);
    let xhr = new XMLHttpRequest();
    let url ='https://sandbox.checkbook.io/v3/invoice';
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Authorization', "9eb04080daf74da76074eff1be227371:c75c4dd7b6f2fea01b3c28c98acacaff");
    
    xhr.send(JSON.stringify(payload));
    
}

