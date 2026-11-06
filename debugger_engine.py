import bdb
import io
import sys
from contextlib import redirect_stdout

class BdbStepDebugger(bdb.Bdb):
    """Real step-by-step Python debugger using standard library bdb."""
    def __init__(self, breakpoints=None):
        super().__init__()
        self.target_breakpoints = set(breakpoints or [])
        self.steps = []

    def user_line(self, frame):
        # Ignore internal frames outside user script
        if frame.f_code.co_filename != "<novacode>":
            return
        line_no = frame.f_lineno
        safe_locals = {
            k: repr(v) for k, v in frame.f_locals.items()
            if not k.startswith("__")
        }
        self.steps.append({
            "line": line_no,
            "function": frame.f_code.co_name,
            "locals": safe_locals,
            "is_breakpoint": line_no in self.target_breakpoints
        })

    def collect_trace(self, source_code: str):
        compiled = compile(source_code, "<novacode>", "exec")
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.run(compiled, {"__name__": "__main__"})
        return self.steps