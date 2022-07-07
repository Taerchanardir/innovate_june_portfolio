

function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}


function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}




function mOver(obj) {
   obj.innerHTML = "<br> HELLO"
   // console.log("mouse over");
}

function mOut(obj) {
    obj.innerHTML = ""
}


function sendAlert() {
    alert(location.hostname);
}

// save the bool 'value', converted to a string, in local storage (for just this window, or the whole site?)
function setIsDarkMode(value){
    let valueAsString = value ? "true" : "false";
    window.localStorage.setItem('dark_mode',valueAsString); // works
    //let isDarkMode=window.localStorage.getItem("dark_mode");
    //console.log(isDarkMode)
}

// get the dark mode setting, as a bool, from the stored string
function getDarkMode(){
    console.log("getDarkMode called");
   let isDarkMode=window.localStorage.getItem("dark_mode"); // it is a string
   if(isDarkMode==="true"){
    console.log("true");
    return true;
   }
   console.log("false");
   return false;
}

// called from the button onClick()
function toggleDarkMode(){
    console.log("toggle");
    let element=document.body;
    element.classList.toggle("dark_mode");
    // how to get what it currently is?

    let isDarkMode=element.classList.contains("dark_mode"); // this works
    //console.log(isDarkMode); // works. it's a bool type
    setIsDarkMode(isDarkMode)


    // the given example
    let mainBox = document.getElementsByClassName("main-box"); // make a list of all elements with "main-box"
    let mainText = document.getElementsByClassName("main-text")
    
    for(const i of mainBox){ // go through each element in the list mainBox and toggle the class dark_modeb in or out
        i.classList.toggle("dark_modeb")
    }
    for(const i of mainText){
        i.classList.toggle("dark_modeb")
    }
    // I missed what "dark_modeb" was.........

}

// read the state from storage, and toggle it on if needed
function initDarkMode(){
    if(getDarkMode()){    // if localstorage says it is true
        toggleDarkMode(); // toggle the dark_mode element in, because page always starts with it not there....does this work for soft page reloads as well as hard page reloads?
    }
}


// added initDarkMode here, because I don't know how to call 2 onLoad's for a page
// checkCookies throws an error when called from the other pages, innerHTML is not found
function checkCookies() {
    let text = ""
    //console.log(navigator.cookiesEnabled); // always disabled, whatever settings I change. Console log says 'undefined'
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
    
}

function checkDarkMode(){
    initDarkMode();
}


// it is persitent on the index.html, but doesn't work on other pages, even though the onLoad is the same...because the main bit of CheckCookies throws an error on the other pages apart from index.html
// it does work with the initDarkMode() done first, because the cookie check code throws an error and stops the function

// with checkDarkMode() as a seperate function in the onLoad, it all works properly...