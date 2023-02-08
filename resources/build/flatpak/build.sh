cd resources/build/flatpak
pip install --upgrade pip
pip install requirements-parser
python3 flatpak-pip-generator  --runtime='org.freedesktop.Sdk//22.08' --requirements-file='requirements.txt' --output pypi-dependencies
flatpak-builder --state-dir='../../../../flat_state' --user --install --force-clean ../../../../flat ../../../org.aimodels.aiy.json --force-clean
