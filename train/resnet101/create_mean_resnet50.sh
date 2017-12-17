#!/usr/bin/env sh
# This script converts the cifar data into leveldb format.
set -e

EXAMPLE=examples
DBTYPE=lmdb

echo "Computing image mean..."

caffe/build/tools/compute_image_mean -backend=$DBTYPE \
  $EXAMPLE/resnet_train_$DBTYPE $EXAMPLE/resnet50_mean.binaryproto

echo "Done."
