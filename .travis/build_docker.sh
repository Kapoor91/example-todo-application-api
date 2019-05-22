#!/bin/sh
set -ev

docker build -t $DOCKER_REPO:$TRAVIS_BRANCH-$COMMIT .

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

if [ "$TRAVIS_BRANCH" == "master" ]; then
    docker tag $DOCKER_REPO:$TRAVIS_BRANCH-$COMMIT $DOCKER_REPO:latest
fi


docker push $DOCKER_REPO