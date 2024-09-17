#!/usr/bin/node
/* eslint-env node */
/* eslint semi: ["error", "always"] */

const request = require('request');
const args = process.argv.slice(2);

if (args.length !== 1) {
  console.log('Usage: node ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = args[0];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }

  const characterUrls = body.characters || [];
  function fetchCharacter (index) {
    if (index >= characterUrls.length) {
      return;
    }

    request(characterUrls[index], { json: true }, (err, res, body) => {
      if (err) {
        console.error('Error:', err);
        process.exit(1);
      }

      console.log(body.name);
      fetchCharacter(index + 1);
    });
  }
  fetchCharacter(0);
});
