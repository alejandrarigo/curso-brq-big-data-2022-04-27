#!/bin/bash

docker run --network singlenode_default --name consumer consumer
docker run --network singlenode_default --name producer producer