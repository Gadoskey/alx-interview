#!/usr/bin/node

/*
  Author: Yusuf Mustapha Opeyemi
  Desc: Writing a script that checks the fetches the content of a webpagewith axios
  
  Still Playing with API

*/

const axios = require("axios");

async function fetchWebsite(url) {
  try {
    // Make the GET request to the website
    const response = await axios.get(url);

    // Handle the response
    console.log("Website fetched successfully!");
    console.log("Status Code:", response.status); // e.g., 200
    console.log("Content:", response.data); // The content of the webpage
  } catch (error) {
    // Handle any errors
    console.error("Error fetching website:", error);
  }
}

const url = "https://gadoski.tech"; 
fetchWebsite(url);
