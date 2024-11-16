#!/usr/bin/node

/*
  Author: Yusuf Mustapha Opeyemi
  Desc: Writing a script that fetches planets:
    name,
    diameter, 
    climate, 
    gravity, 
    terrain, 
    surface_water, 
    population
  from a specified Star Wars movie using the Star Wars API.
  The Movie ID is passed as a command-line argument.
  
  Still Playing with API

*/

const request = require("request")

function fetchPlanetsData(id) {
  const url = `https://swapi.dev/api/films/${id}/`;

  // Fetch movie data

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetcing details: ${error}`);
      return;
    }
    if (response.statusCode !== 200) {
      console.error("Error: Movie not found or invalid Movie ID");
      return;
    }

    const movieData = JSON.parse(body);

    // Fetch planets url

    const planetPromises = movieData.planets.map((planetsUrl) => {
      return new Promise((resolve, reject) => {
        request(planetsUrl, (planetError, planetResponse, planetBody) => {
          if (planetError) {
            reject(
              new Error("Error fetching character details: " + planetError)
            );
          } else if (planetResponse.statusCode === 200) {
            const planetData = JSON.parse(planetBody);
            resolve({
              name: planetData.name,
              diameter: planetData.diameter,
              climate: planetData.climate,
              gravity: planetData.gravity,
              terrain: planetData.terrain,
              surface_water: planetData.surface_water,
              population: planetData.population,
            });
          } else {
            reject(new Error("Error: Character not found"));
          }
        });
      });
    });

    // iterate through planetPromises and print data

    let i = 1;
    Promise.all(planetPromises)
      .then((planets) => {
        planets.forEach((planet) => {
          console.log(`Planet: ${i}`);
          console.log(`Name: ${planet.name}`);
          console.log(`Diameter: ${planet.diameter}`);
          console.log(`Climate: ${planet.climate}`);
          console.log(`Gravity: ${planet.gravity}`);
          console.log(`Terrain: ${planet.terrain}`);
          console.log(`Surface: ${planet.surface_water}`);
          console.log(`Population: ${planet.population}`);
          console.log(`End of Planet ${i}`);
          i++;
        });
      })
      .catch((err) => console.error(err));
  });
}

// Get the Movie ID from the command line arguments
const id = process.argv[2];

if (!id) {
  console.log("Usage: ./script.js <Movie ID>");
} else {
  fetchPlanetsData(id);
}