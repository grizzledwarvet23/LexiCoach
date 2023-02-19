function changeText() {
    document.getElementById("create-vocablist-btn").innerHTML = "VocabList Created!";
}

function goToVocabListWindow() {
    window.location.href = "/create-vocablist";
}

function goToHomeWindow() {
    //print("hello");
    var l_element = document.getElementById("language");
    var lan = l_element.options[l_element.selectedIndex].text;
    var _name = document.getElementById("vocablist-title").value;
    var terms_no = document.getElementById("terms-container").childElementCount;
    var terms_tot = ""
    for(let i = 1; i <= terms_no; i++){
        if (document.getElementById("term" + i).value != ""){
            if(i != 1){
                terms_tot = terms_tot + ",";
            }
            terms_tot = terms_tot + document.getElementById("term" + i).value;
        }

    }
    window.location.href = "/addlist?name=" + _name + "&language=" + lan + "&vocab=" + terms_tot;
    
}

function goToDonatePage() {
    window.location.href = "/donate";
}

function startPractice(el){
    el.style.backgroundColor = "#85C1E9"
    window.location.href = "/practice?listname=" + el.innerHTML

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

function grade(){
    var num_s = document.getElementById("mainform").childElementCount - 1;
    var num_r = 0;
    for(let i = 1; i <= num_s; i++){
        document.getElementById("label"+i).innerHTML = document.getElementById("word"+i).getAttribute("fullse")
        if(document.getElementById("word"+i).value.toLowerCase() == document.getElementById("word"+i).getAttribute("cans").toLowerCase()){
            document.getElementById("word"+i).style.color = "green"
            document.getElementById("word"+i).style.backgroundColor = "#82E0AA"
            num_r += 1;
        }
        else{
            document.getElementById("word"+i).style.color = "#7B241C"
            document.getElementById("word"+i).style.backgroundColor = "#F1948A"
        }
    }
    document.getElementById("scoreholder").innerHTML = "You got " + num_r + " of " + num_s + "."
    document.getElementById("grader").innerHTML = "Home"
    document.getElementById("grader").setAttribute("onclick","gohome()")
}
function gohome(){
    window.location.href = "/"
}

function handleDonate(event) {
    window.location.href = "/";
    event.preventDefault();

    const options = {
        method: 'POST',
        //mode: 'no-cors',
        headers: {
          accept: 'application/json',
          'content-type': 'application/json',
          Authorization: '9eb04080daf74da76074eff1be227371:c75c4dd7b6f2fea01b3c28c98acacaff',
          'Access-Control-Allow-Origin':'*',
          'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
        },
        
        body: JSON.stringify({
            "amount": parseFloat(document.getElementById('amount').value),
            "description": document.getElementById('message').value,
            "name": document.getElementById('name').value,
            "recipient": document.getElementById('email').value
        })
      };
    
    console.log(options);
    
    fetch('http://localhost:8010/proxy/v3/invoice', options)
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(err => console.error(err));
     
}

