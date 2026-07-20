import os
from flask import Flask, render_template

app = Flask(__name__)

# --- Optional tip jar config ---
# To enable: generate your own PayNow QR code from your banking app
# (DBS/OCBC/UOB etc. all have a "Share/Save PayNow QR" option) and save
# it as static/assets/paynow_qr.png. Or set TIP_LINK to a Ko-fi/Buy Me
# a Coffee URL instead. Both are optional — leave as-is to skip the tip
# jar entirely. Neither of these contains real payment data.
TIP_QR_RELATIVE_PATH = "assets/paynow_qr.png"  # relative to the static/ folder
TIP_LINK = ""  # e.g. "https://ko-fi.com/yourname"


@app.route("/")
def index():
    qr_full_path = os.path.join(app.static_folder, TIP_QR_RELATIVE_PATH)
    tip_qr_url = f"/static/{TIP_QR_RELATIVE_PATH}" if os.path.exists(qr_full_path) else None
    return render_template("index.html", tip_qr_url=tip_qr_url, tip_link=TIP_LINK)


if __name__ == "__main__":
    # Railway (and most PaaS hosts) inject PORT dynamically — fall back to
    # 8080 for local testing.
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
