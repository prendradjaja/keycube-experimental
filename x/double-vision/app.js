const globalState = { // TODO rename to globals
  angle: 'right',
  startTime: undefined,
  alreadySolved: true,
};
const cube = new Cube(); // TODO move to globalState
draw(cube);

document.addEventListener('keydown', event => {
  const move = getMove(event);
  if (event.code === 'Tab') {
    event.preventDefault();
    globalState.angle = otherAngle(globalState.angle);
    draw(cube);
    return;
  } else if (event.code === 'Space' && globalState.alreadySolved) {
    scramble();
    return;
  } else if (!move) {
    return;
  }

  cube.move(move);
  draw(cube);
  if (cube.isSolved() && !globalState.alreadySolved) {
    const solveTime = (new Date().valueOf() - globalState.startTime) / 1000;
    console.log('Solved in: ' + solveTime);
    document.querySelector('button#scramble').disabled = false;
    globalState.alreadySolved = true;
  }
});

function scramble() {
  cube.init(Cube.random());
  draw(cube);
  document.querySelector('button#scramble').disabled = true;
  globalState.startTime = new Date().valueOf();
  globalState.alreadySolved = false;
}
