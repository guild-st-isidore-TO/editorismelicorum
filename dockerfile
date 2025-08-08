# this file uses the "--break-system-packages" flag to workaround a common error:
# 
# error: externally-managed-environment
# × This environment is externally managed
# ╰─>
#     The system-wide python installation should be maintained using the system
#     package manager (apk) only.
#     If the package in question is not packaged already (and hence installable via
#     "apk add py3-somepackage"), please consider installing it inside a virtual
#     environment, e.g.:
#     python3 -m venv /path/to/venv
#     . /path/to/venv/bin/activate
#     pip install mypackage
#     To exit the virtual environment, run:
#     deactivate
#     The virtual environment is not deleted, and can be re-entered by re-sourcing
#     the activate file.
#     To automatically manage virtual environments, consider using pipx (from the
#     pipx package).
# note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
# hint: See PEP 668 for the detailed specification.
# 
# see:
# - https://www.makeuseof.com/fix-pip-error-externally-managed-environment-linux/

FROM alpine:latest
RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --upgrade pip --break-system-packages
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt --break-system-packages
CMD ["python3", "app.py"]
