// JavaScript Native Browser Engine
function analyzeMetrics(requests) {
  const total = requests.reduce((acc, n) => acc + n, 0);
  const avg = (total / requests.length).toFixed(2);
  console.log("Processed metrics -> Total:", total, "Avg:", avg);
  return { total, avg };
}

analyzeMetrics([120, 240, 180, 310]);