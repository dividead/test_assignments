const util = require("util")
const exec = util.promisify(require("child_process").exec)

var cmds = ["echo 1", "echo 2", "echo 3"]

async function runner(arr) {
  for (let cmd of arr) {
    await exec(cmd)
  }
}
runner(cmds)
