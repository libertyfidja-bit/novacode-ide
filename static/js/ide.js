// Frontend Controller connecting Editor, Python Tracer & Git Sync
export async function runDebugSession(code, breakpoints) {
  const response = await fetch("/api/debug", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code, breakpoints })
  });
  return await response.json();
}