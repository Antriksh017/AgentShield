from datetime import datetime
import os
import re

def save_html_report(scenario_name, messages):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/{scenario_name}_{timestamp}.html"
    os.makedirs("reports", exist_ok=True)

    rows = ""
    for msg in messages:
        sender = msg.get("name", "unknown")
        content = msg.get("content", "")
        if not content:
            continue

        # Skip raw JSON blobs
        stripped = content.strip()
        if stripped.startswith("{") or stripped.startswith("[{"):
            continue

        # Convert markdown table to HTML table
        if "|" in content:
            lines = content.strip().split("\n")
            table_html = "<table>"
            for i, line in enumerate(lines):
                if line.strip().startswith("|"):
                    cols = [c.strip() for c in line.strip().strip("|").split("|")]
                    if all(set(c) <= set("-| ") for c in cols):
                        continue
                    tag = "th" if i == 0 else "td"
                    table_html += "<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cols) + "</tr>"
            table_html += "</table>"
            content = table_html
        else:
            content = f"<pre>{content}</pre>"

        rows += f"""
        <div class="message">
            <div class="sender">{sender}</div>
            <div class="content">{content}</div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{scenario_name} Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #0d1117; color: #c9d1d9; padding: 30px; max-width: 1200px; margin: auto; }}
        h1 {{ color: #58a6ff; font-size: 28px; }}
        .meta {{ color: #8b949e; margin-bottom: 30px; font-size: 13px; }}
        .badge {{ background: #1f6feb; color: white; padding: 3px 10px; border-radius: 20px; font-size: 12px; margin-left: 10px; }}
        .message {{ background: #161b22; border-left: 4px solid #58a6ff; margin: 20px 0; padding: 20px; border-radius: 8px; }}
        .sender {{ color: #f78166; font-weight: bold; margin-bottom: 10px; font-size: 13px; text-transform: uppercase; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; margin: 0; font-size: 13px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 10px; }}
        th {{ background: #1f6feb; color: white; padding: 10px 14px; text-align: left; }}
        td {{ padding: 9px 14px; border-bottom: 1px solid #30363d; font-size: 13px; }}
        tr:hover td {{ background: #1c2128; }}
        .footer {{ margin-top: 40px; color: #484f58; font-size: 12px; text-align: center; }}
    </style>
</head>
<body>
    <h1>🛡️ {scenario_name} <span class="badge">Antriksh Gupta</span></h1>
    <div class="meta">Generated: {timestamp} &nbsp;|&nbsp; Powered by Ollama Qwen3 + AutoGen</div>
    {rows}
    <div class="footer">cyber-security-llm-agents &nbsp;|&nbsp; github.com/Antriksh017</div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✅ Report saved to: {filename}")
    return filename