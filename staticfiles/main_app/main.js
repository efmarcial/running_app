// Get the container element
var btnContainer = document.getElementById("bottomTab");

// Get all buttons with class="bloc-icon" inside the container
var btns = btnContainer.getElementsByClassName("bloc-icon");

// Loop through the buttons and ass the active class to
// the current/clicked button
for(var i = 0; i < btns.length; i++){
    btns[i].addEventListener("click", function(){
        var current = document.getElementsByClassName("active-bottom");


        current[0].className = current[0].className.replace("active-bottom", "");
        this.className += " active-bottom";
    });
}