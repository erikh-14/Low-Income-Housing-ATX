function load_page(url) {
    window.location.href=url
}

// Retrieve a cookie name
function get_cookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
}


function checkCookie() {
  var user=get_cookie("username");
  if (user != "") {
    console.log(user);
  } else {
     user = alert("You will now be redirected to the Login Page");
     location.href = 'index.html';
     }
  }
