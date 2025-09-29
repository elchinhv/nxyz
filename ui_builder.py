import subprocess
from java import jclass

TextView = jclass("android.widget.TextView")

# Run a shell command (here we list files in app's internal storage)
# Adjust the path as needed: /data/data/<your.package.name>/files
result = subprocess.run(
    ["ls", "/data/data/" + ctx.getPackageName() + "/files"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# If ls fails, fallback to echo
output = result.stdout.strip() or result.stderr.strip()
if not output:
    output = "No files found or command failed"

new_text = TextView(ctx)
new_text.setText(output)
new_text.setTextSize(20.0)

parent.addView(new_text)