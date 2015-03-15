var stdin = process.openStdin(); 
process.stdin.setRawMode();

stdin.on('keypress', function (chunk, key) {
  process.stdout.write('Get Chunk: ' + chunk + '\n');

  while(true){
      console.log("Hello");
     if (key && key.ctrl && key.name == 'c') process.exit(); 
  }
  if (key && key.ctrl && key.name == 'c') process.exit();
});