SONARQUBE_URL="localhost:8080"
YOUR_PROJECT_KEY="CodeReviewTest"
YOUR_REPO=$(pwd)

docker run \
    --rm \
    -e SONAR_HOST_URL="http://${SONARQUBE_URL}" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=${YOUR_PROJECT_KEY}" \
    -e SONAR_TOKEN="myAuthenticationToken" \
    -v "${YOUR_REPO}:/usr/src" \
    --network=host \
    sonarsource/sonar-scanner-cli