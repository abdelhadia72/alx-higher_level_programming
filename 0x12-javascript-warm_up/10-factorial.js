#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = [];
  for (let i = 2; i < process.argv.length; i++) {
    args.push(process.argv[i]);
  }
  args.sort()
  console.log(args[args.length - 2]);
}
