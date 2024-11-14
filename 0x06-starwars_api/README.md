# Star Wars Characters Script

## Author
**Yusuf Mustapha Opeyemi**

## Overview
This Node.js script fetches and prints the names of all characters from a specified Star Wars movie, using the [Star Wars API (SWAPI)](https://swapi.dev/). It displays each character name in the order they appear in the API's `characters` list. The script uses the `request` module for handling HTTP requests.

## Requirements
- **Node.js** installed on your system
- **request** module installed

## Installation
1. **Install Node.js** if you haven't already: [Download and install Node.js](https://nodejs.org/).
2. **Install the request module** by running:
   ```bash
   npm install request

## Usage
1. Make the script executable by running:
`chmod +x script.js`
2. Run the script with a Movie ID as a command-line argument:
`./script.js <Movie ID>`
### Replace <Movie ID> with the Star Wars movie ID:
1 - A New Hope
2 - The Empire Strikes Back
3 - Return of the Jedi
4 - The Phantom Menace
5 - Attack of the Clones
6 - Revenge of the Sith
7 - The Force Awakens
### Example
To get characters from "Return of the Jedi" (Movie ID 3):
`./script.js 3`

## Expected Output
The script will print each character name on a new line in the order they appear in the movie's characters list.

## Error Handling
- If an invalid Movie ID is provided, the script will output an error message.
- If a character's details cannot be fetched, an error message will be displayed.

## License
This project is open-source and free to use.

### Explanation of `README.md` Contents:

- **Author**: Lists the author's name.
- **Overview**: Briefly explains the script’s functionality.
- **Requirements**: Details any dependencies, such as Node.js and the `request` module.
- **Installation**: Provides steps to install necessary components.
- **Usage**: Explains how to execute the script, with examples.
- **Expected Output**: Describes the output format.
- **Error Handling**: Highlights how the script manages errors.
- **License**: Marks it as open-source for easy usage.