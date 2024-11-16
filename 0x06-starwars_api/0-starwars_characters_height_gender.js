#!/usr/bin/node
/*
Author: Yusuf Mustapha Opeyemi
Description: This script fetches and prints all character names, gender, and height
  from a specified Star Wars movie using the Star Wars API.
  The Movie ID is passed as a command-line argument.
  Playing with API
*/

const request = require("request");

function fetchMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  // Fetch movie data
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Error: Movie not found or invalid Movie ID');
      return;
    }

    const movieData = JSON.parse(body);

    // Map each character URL to a promise that fetches the character's name
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(new Error('Error fetching character details: ' + charError));
          } else if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            resolve({
              name: characterData.name,
              skin_color: characterData.skin_color,
              eye_color: characterData.eye_color
            });
          } else {
            reject(new Error('Error: Character not found'));
          }
        });
      });
    });


    // Resolve all promises in order and print each character name
    Promise.all(characterPromises)
      .then((characters) => {
        characters.forEach((character) => {
          console.log("**** **** **** ****");
          console.log(character.name);
          console.log(character.skin_color);
          console.log(character.eye_color);
          console.log("**** **** **** ****");
        });
      })
      .catch((err) => console.error(err));
  });
}

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./script.js <Movie ID>');
} else {
  fetchMovieCharacters(movieId);
}
