const maxValue = (arr, index) => {
  const left = index * 2 + 1
  const right = index * 2 + 2

  let max = left
  if (arr[left] < arr[right]) {
    max = right
  }
  if (arr[index] > arr[max]) {
    max = false
  }

  return max
}

const swapper = (a, i, j) => ([a[i], a[j]] = [a[j], a[i]])

const maxHeap = (arr) => {
  let breakFor = false

  for (let index = 0; index < Math.floor(arr.length / 2); index++) {
    const maxIndex = maxValue(arr, index)
    if (maxIndex) {
      swapper(arr, maxIndex, index)
      breakFor = true
      break
    }
  }
  if (breakFor) {
    maxHeap(arr)
  }
}

const confirm = (arr) => {
  for (let index = 0; index < arr.length - 1; index++) {
    if (arr[index] > arr[index + 1]) {
      return false
    }
  }
  return true
}

const maxHeapSort = (arr) => {
  maxHeap(arr)
  const orderedArr = []
  const arrLength = arr.length - 1

  for (let index = 0; index < arrLength; index++) {
    const lastPosition = arrLength - index
    swapper(arr, lastPosition, 0)
    orderedArr.splice(0, 0, arr.pop())
    maxHeap(arr)
  }
  const valid = confirm(arr)
  if (valid) {
    return orderedArr
  }
  return false
}

module.exports = { maxHeapSort }
