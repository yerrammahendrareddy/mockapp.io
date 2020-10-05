import os
import json

from flask import Blueprint
from flask import render_template
from flask_login import login_required
from flask import flash
from flask import current_app

from mockapp.enhance import base_context
from mockapp.html import notify_success

mock_app_blueprint = Blueprint(
    "mock_app",
    __name__,
    template_folder="templates",
    url_prefix="/mock_app",
)
all_info = {}

@mock_app_blueprint.route("/")
@login_required
def index():
    context = base_context()

    for module in os.listdir(os.path.join(current_app.config['BASE_DIR'], "modules")):
        if module.startswith("__"):
            continue
        if module not in ["mock_app"]:
            with open(os.path.join(current_app.config['BASE_DIR'], 'modules', module, 'info.json')) as f:
                module_info = json.load(f)
                all_info[module] = module_info

    context["all_info"] = all_info
    flash(notify_success('Notif test'))
    return render_template("mock_app/index.html", **context)
