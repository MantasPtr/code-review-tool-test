for FILE in ./examples/*; do
    /Users/mape/code-review-tool-test/venv/bin/python3 /Users/mape/code-review-tool-test/gptscan.py -u "$FILE" > out/$(basename "$FILE").txt;
done