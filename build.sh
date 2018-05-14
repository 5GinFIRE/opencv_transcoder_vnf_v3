#!/bin/bash

mkdir opencv_transcoder_vnf
cp -r vnf/* opencv_transcoder_vnf
cp -r charms opencv_transcoder_vnf
cd opencv_transcoder_vnf
find * -type f -print | while read line; do md5sum $line >> checksums.txt; done
cd ..
tar -czvf opencv_transcoder_vnf.tar.gz opencv_transcoder_vnf
rm -rf opencv_transcoder_vnf

mkdir opencv_transcoder_ns
cp -r ns/* opencv_transcoder_ns
cd opencv_transcoder_ns
find * -type f -print | while read line; do md5sum $line >> checksums.txt; done
cd ..
tar -czvf opencv_transcoder_ns.tar.gz opencv_transcoder_ns
rm -rf opencv_transcoder_ns
