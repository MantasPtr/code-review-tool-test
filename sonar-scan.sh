SONARQUBE_URL="localhost:9001"
YOUR_PROJECT_KEY="code-review-tool-test"
YOUR_REPO=$(pwd)
TOKEN=$SONAR_TOKEN



docker run \
    --rm \
    -e SONAR_HOST_URL="http://${SONARQUBE_URL}" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=${YOUR_PROJECT_KEY}" \
    -e SONAR_TOKEN="${TOKEN}" \
    -v "${YOUR_REPO}:/usr/src" \
    --network=host \
    sonarsource/sonar-scanner-cli