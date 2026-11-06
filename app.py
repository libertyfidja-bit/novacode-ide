from flask import Flask, render_template, request, jsonify
from debugger_engine import BdbStepDebugger
from git_sync import GitRepoClient

app = Flask(__name__)
git_client = GitRepoClient()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def run_code_route():
    payload = request.get_json() or {}
    code_str = payload.get("code", "")
    debugger = BdbStepDebugger()
    output, error = debugger.execute_script(code_str)
    return jsonify({"output": output, "error": error})

@app.route("/api/debug", methods=["POST"])
def debug_code_route():
    payload = request.get_json() or {}
    code_str = payload.get("code", "")
    breakpoints = payload.get("breakpoints", [8, 14])
    tracer = BdbStepDebugger(breakpoints=breakpoints)
    trace_steps = tracer.collect_trace(code_str)
    return jsonify({"steps": trace_steps, "total_steps": len(trace_steps)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)