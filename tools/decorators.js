const now = require("performance-now")
const process = require('process')

class Statistics {
  constructor(stats) {
    this.stats = stats
  }

  print(){

    const YELLOW = `\x1b[33m`;
    const RED = `\x1b[31m`;
    const NORMAL = `\x1b[0m`;
    const BOLD = `\x1b[1m`;

    const inconsistent_message = this.stats.arr_len != this.stats.arr_result_len ? `${YELLOW} ⚠ WARNING: inconsistent length${NORMAL}` : "";
    const valid_sort_message = `List ${this.stats.valid_sort ? "": `${RED}NOT ${NORMAL}`}sorted correctly`;

    console.log(
      `'${BOLD}${this.stats.function_name}${NORMAL}' statistics
      ${valid_sort_message}
      array length: ${this.stats.arr_len} - result array length: ${this.stats.arr_result_len}${inconsistent_message}
      order time: ${this.stats.total_time}
      memory used: ${this.stats.used_size_memory}KiB`
    );
  }
}

const verifier = (arr) => {
  for (let index = 0; index < arr.length - 1; index++) {
    if (arr[index] > arr[index + 1]) {
      return false;
    }
  }
  return true;
}

const statistics = (func) => {
  return (args) => {
    const arrLength = args.length
    mem1 = process.memoryUsage()
    const startTime = now();
    const result = func(args);
    mem2 = process.memoryUsage()
    const endTime = now();

    const stats_object = {
      "function_name": func.name,
      "arr_len": arrLength,
      "arr_result_len": result.length,
      "valid_sort": verifier(result),
      "total_time": endTime - startTime,
      "used_size_memory": mem2.heapUsed - mem1.heapUsed,
    }
    return { result, statistics: new Statistics(stats_object) };
  }
}

module.exports = statistics;
