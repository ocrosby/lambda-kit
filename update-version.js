const fs = require('fs');
const path = require('path');

const filePath = path.resolve('pyproject.toml')
const version = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const updatedData = data.replace(/version = ".*"/, `version = "${version}"`);

  fs.writeFile(filePath, updatedData, 'utf8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});