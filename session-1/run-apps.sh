docker run -ti \
    -v "$(pwd)/apps.py:/script/apps.py" \
    python3-session \
    python3 /script/apps.py