const debounce = (f, delta, nextCall) => cb => {
  if (!nextCall || nextCall <= Date.now()) {
    nextCall = Date.now() + delta
    f(cb())
  }
}

let log = debounce(console.log, 1000)

setInterval(log, 10, () => new Date())
