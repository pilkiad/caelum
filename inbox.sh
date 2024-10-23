echo "+-- TASK INBOX ($(grep -r '# TODO' --include '*.py' --exclude-dir=venv . | wc -l))"
echo "|"
grep -nr '# TODO' --include '*.py' --exclude-dir=venv . | xargs -I {} echo "| "{}
echo "|"
echo "+--"

echo "+-- ERROR INBOX ($(grep -r '# FIXME' --include '*.py' --exclude-dir=venv . | wc -l))"
echo "|"
grep -nr '# FIXME' --include '*.py' --exclude-dir=venv . | xargs -I {} echo "| "{}
echo "|"
echo "+--"
