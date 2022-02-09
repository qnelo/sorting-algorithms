const randomArray = (arrayLength, biggestNumber) => {
  const arr = []
  for (let index = 0; index < arrayLength; index++) {
    arr.push(Math.round(Math.random() * biggestNumber))
  }
  return arr
}

module.exports = { randomArray }
