console.log("Running loginPageRequest.js!");

// Sends a JSON Object to the back-end using a dictionary
function send_login(login_dictionary){
  //API key for connection
  console.log("send_login() is called!");
  var url = 'api/login';
  var jsonObject = JSON.stringify(login_dictionary);

  //making a bridge to the web server
  var request = new XMLHttpRequest();
  //initializing request to the web server
  request.open('POST',  url, true);
  //Setting the header of the API request
  request.setRequestHeader("Content-type", "application/json");

  //do something with the data being processed
  request.onload = function()
  {
   console.log("request.onload is called!");

    // Good response
    if (request.status >= 200 && request.status < 400){
      console.log("Request is sent!");
      console.log("Response: " + request.response);
      console.log(request.statusText);
      document.cookie = "username = " + login_dictionary["username"];
//      names_dictionary = JSON.parse(request.response);
//      document.cookie = "firstname = " + names_dictionary["first_name"];
//    document.cookie = "lastname = " + names_dictionary["last_name"];
      location.replace("http://67.205.136.114/maindash.html");

    }

    // Bad Response, error handling
    else {
      console.log(request.status);
      alert ("Login error: " + request.status + " (" + request.response +  ")");
    }
  }

  // Send JSON Object to back-end
	request.send(jsonObject);
  return false;
}

// Sends a JSON Object to the back-end using a dictionary
function send_adminlogin(login_dictionary){
  //API key for connection
  console.log("send_adminlogin() is called!");
  var url = 'api/adminLogin';
  var jsonObject = JSON.stringify(login_dictionary);

  //making a bridge to the web server
  var request = new XMLHttpRequest();
  //initializing request to the web server
  request.open('POST',  url, true);
  //Setting the header of the API request
  request.setRequestHeader("Content-type", "application/json");

  //do something with the data being processed
  request.onload = function()
  {
   console.log("request.onload is called!");

    // Good response
    if (request.status >= 200 && request.status < 400){
      console.log("Request is sent!");
      console.log("Response: " + request.response);
      console.log(request.statusText);
      document.cookie = "username = " + login_dictionary["username"];
//      names_dictionary = JSON.parse(request.response);
//      document.cookie = "firstname = " + names_dictionary["first_name"];
//    document.cookie = "lastname = " + names_dictionary["last_name"];
      location.replace("http://67.205.136.114/adminDash.html");

    }

    // Bad Response, error handling
    else {
      console.log(request.status);
      alert ("Login error: " + request.status + " (" + request.response +  ")");
    }
  }

  // Send JSON Object to back-end
	request.send(jsonObject);
  return false;
}