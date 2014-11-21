$(document).ready(function () {

    
    // Change My Color
    var colLeft = document.getElementById('left-column');

    function touchStart(event) {
        event.preventDefault();
        colLeft.style.backgroundColor = '#69D2E7';
        colLeft.style.color = '#000';
    };
    
    function touchEnd(event) {
        event.preventDefault();
        colLeft.style.backgroundColor = 'transparent';
        colLeft.style.color = '#fff';
    }
        

    colLeft.addEventListener('touchstart', touchStart, false);
    colLeft.addEventListener('touchend', touchEnd, false);
    

    // Where Am I?
    var locReq = document.getElementById('location');
    var locBtn = document.getElementById('location-button');
    
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        }
        else {
            locReq.innerHTML = "Geolocation is not supported by your browser!";}
    }
    
    function showPosition(position) {
        locReq.innerHTML = "Your Latitude: " + position.coords.latitude + "<br/>Your Longitude: " + position.coords.longitude;
        locBtn.style.display = 'none';
    }
    
    locBtn.addEventListener('click', getLocation, false);
    
    
    // Battery Status
    var battery = navigator.battery || navigator.webkitBattery || navigator.mozBattery;
    
    if (battery) {
        var node = document.getElementById('batteryLevel');
        var change = function(e) {
            var percentage = (battery.level * 100) + "%";
            node.style.width = percentage;
            node.innerHTML = percentage;
        };
        
        change();
    }
    else {
        alert("Sorry, your current browser cannot detect your battery level. Try viewing this page in Mozilla Firefox, Chrome, or Opera on your desktop! It works there. :)");
    }
    
});

