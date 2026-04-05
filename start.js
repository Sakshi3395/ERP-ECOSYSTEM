const { exec } = require('child_process');
const path = require('path');

const venvActivate = path.join(__dirname, 'backend', 'venv', 'Scripts', 'activate');
const backendRun = 'python backend/run.py';
const frontendRun = 'npm run dev --prefix frontend';

function runCommand(command, name) {
  const proc = exec(command, { shell: true });
  proc.stdout.on('data', data => process.stdout.write(`[${name}] ${data}`));
  proc.stderr.on('data', data => process.stderr.write(`[${name} ERROR] ${data}`));
  proc.on('close', code => console.log(`[${name}] exited with code ${code}`));
  return proc;
}

console.log('Checking and activating venv...');
runCommand(`cmd /c "cd backend && venv\\Scripts\\activate && python run.py"`, 'backend');
setTimeout(() => {
  console.log('Starting frontend...');
  runCommand(frontendRun, 'frontend');
}, 4000);
