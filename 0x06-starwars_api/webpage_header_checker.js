#!/usr/bin/node

/*
  Author: Yusuf Mustapha Opeyemi
  Desc: Writing a script that checks the return type of a webpage
  
  Still Playing with API

*/

const request = require("request");

request("https://gadoski.tech", (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if ((response.statusCode !== 200)) {
    console.errror("Error fetching details");
  }
  console.log(response.headers["content-type"]);
  console.log(body);
});
