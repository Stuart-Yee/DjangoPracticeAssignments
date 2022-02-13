console.log("yo!");

window.onload = function() {
    console.log("window loaded");

    var createButton = document.getElementById("createBtn");
    var users = document.getElementsByClassName("user_records");

    createButton.onclick = function (){
        var name = document.getElementById("first_name").value;
        alert("You definitely clicked that, so we're going to add " + name);
    }


    console.log(users);
    console.log(users[users.length-1]);
    console.log(users[users.length-1].children[0].outerText);
}