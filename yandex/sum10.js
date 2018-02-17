function tens(a, t, r = []) {
  if (t < 0) return
  for (let i of a) {
    if (i == t) r.push([i])
    let s = tens(a.slice(a.indexOf(i) + 1), t - i)
    if (s) for (let x of s) r.push([i].concat(x))
  }
  return r
}

let arr = [7, 10, 2, 5, 3, 1]
let arr2 = [1, 5, 6, 4, 2, 8]

console.log(tens(arr, 10))
