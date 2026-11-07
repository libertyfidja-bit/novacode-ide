// JavaScript / Node.js Native Runner
function analyzePerformance(scores) {
  const total = scores.reduce((acc, n) => acc + n, 0);
  const average = +(total / scores.length).toFixed(2);
  console.log("Scores:", scores.join(", "));
  console.log("Calculated Average:", average);
  return { total, average, status: average >= 80 ? "PASS" : "REVIEW" };
}

const result = analyzePerformance([88, 94, 79, 91, 85]);
console.log("Result Payload:", JSON.stringify(result));