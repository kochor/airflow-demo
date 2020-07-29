#!/usr/bin/env bash
# Description: Script blocks public access to a bucket

BUCKET_NAME='infutorbucket'

aws s3api put-public-access-block \
    --bucket $BUCKET_NAME \
    --public-access-block-configuration "BlockPublicAcls=true,\
                                          IgnorePublicAcls=true,\
                                          BlockPublicPolicy=true,\
                                          RestrictPublicBuckets=true"
