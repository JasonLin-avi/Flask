docker run --rm -it -v ${PWD}:/scripts \
  artilleryio/artillery:latest \
  run /scripts/test.yaml
