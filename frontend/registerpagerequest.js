console.log("Running registerpagerequest.js")

/*
//Whenever the submit button is click, the user credential will be created
//a json object and send to the python server
var registerObject = $('#my-registration')
{
    regisUserName = document.forms["myForm"]["fname"].value;
    regisPassWord = document.forms["myForm"]["fpass"].value;
    regisLocation = document.forms["myForm"]["flocation"].value;

}

//Getting the submit button for an event listener
var submit = document.getElementById("submit");

//event listenter:
submit.addEventListener( 'submit', function(e) {
    const
})
*/

function send_register(register_dictionary) {
    //API key for connection
    console.log("send_register is called!");
    var url = 'api/register';
    var jsonObject = JSON.stringify(register_dictionary);
    console.log (jsonObject);

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
        alert("Registration of user " + register_dictionary['username'] + " successful!");
        location.replace("http://67.205.136.114/index.html");
      }

      else {

        alert(request.status + " FAILED: Registration of user " + register_dictionary['username'] + " failed! (" + request.response + ")");
        console.log(request.status);
      }
    }

        //request get sent out!
      request.send(jsonObject);
      return false;
}


function send_admin_register(register_dictionary) {
  //API key for connection
  console.log("send_register is called!");
  var url = 'api/adminRegister';
  var jsonObject = JSON.stringify(register_dictionary);
  console.log (jsonObject);

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
      alert("Registration of user " + register_dictionary['username'] + " successful!");
      location.replace("http://67.205.136.114/admin.html");
    }

    else {

      alert(request.status + " FAILED: Registration of user " + register_dictionary['username'] + " failed! (" + request.response + ")");
      console.log(request.status);
    }
  }

      //request get sent out!
    request.send(jsonObject);
    return false;
}