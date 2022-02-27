const statistics = require("../tools/decorators")

/**
 * Get the index of the max value between parent and boot children
 * @param {Array} arr Array to sort
 * @param {Number} index index of the array to compare
 * @returns {Number} max index value, "-1" if parent have the max value
 */
const maxIndexValue = (arr, index) => {
  const left = index * 2 + 1;
  const right = index * 2 + 2;

  let max = left;
  if (arr[left] < arr[right]) {
    max = right;
  }
  if (arr[index] > arr[max]) {
    max = -1;
  }

  return max;
}

const maxHeap = (arr) => {
  // TODO, add as parameter length of array to dont have to create another array
  let breakFor = false;

  for (let index = 0; index < Math.floor(arr.length / 2); index++) {
    const maxIndex = maxIndexValue(arr, index);
    if (maxIndex >= 0) {
      [arr[maxIndex], arr[index]] = [arr[index], arr[maxIndex]];
      breakFor = true;
      break;
    }
  }
  if (breakFor) {
    maxHeap(arr);
  }
}


/**
 * Order an array use Max Heap Sort technique
 * @param {Array} arr array to sort
 * @returns {Boolean} if is ordered
 */
const maxHeapSort = (arr) => {
  maxHeap(arr);
  const orderedArr = [];
  const arrLength = arr.length - 1;

  for (let index = 0; index <= arrLength; index++) {
    const lastPosition = arrLength - index;
    [arr[lastPosition], arr[0]] = [arr[0], arr[lastPosition]]
    orderedArr.splice(0, 0, arr.pop());
    maxHeap(arr);
  }
  return orderedArr;
}

module.exports = { maxHeapSort: statistics(maxHeapSort) }
