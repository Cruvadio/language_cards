var myImage = document.querySelector('img');

myImage.onclick = function()
{
    var mySrc = myImage.getAttribute('src');
    if (mySrc == 'images/american-flag-png-circle-6-original.png'){
        myImage.setAttribute('src', 'images/scale_1200.webp');
    } else {
        myImage.setAttribute('src', 'images/american-flag-png-circle-6-original.png')
    }
}

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
    var myName = prompt('Please enter your name.');
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Welcome, ' + myName;
  }

myButton.onclick = function() {
  setUserName();
}
