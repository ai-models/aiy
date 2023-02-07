#python3 flatpak-pip-generator  --runtime='org.freedesktop.Sdk//22.08' --requirements-file='requirements.txt' --output pypi-dependencies
#flatpak-builder --state-dir='../../../../flat_state' ../../../../flatpak-aiy org.visioninit.Aiy.json --force-clean
flatpak-builder --state-dir='../../../../flat_state' --user --install --force-clean ../../../../flatpack-aiy2 org.visioninit.Aiy.json --force-clean
