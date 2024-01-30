const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node script.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log('File content:', data);
});
