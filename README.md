# OpenCV Transcoder VNF

This repository hosts a OpenCV Video Transcoder VNF. It also contains an example NS descriptor to deploy this VNF.

## Download the VM Image

You can find the VM image [here](https://atnog.av.it.pt/~eduardosousa/opencv_transcoder_image.qcow2).
The VM image should be uploaded with the following name: **opencv_transcoder_image**

## Build the descriptors

To build the descriptors, you must run the following command:

~~~~
./build.sh
~~~~

After running this command, you should have two .tar.gz files:

~~~~
opencv_transcoder_vnf.tar.gz
opencv_transcoder_ns.tar.gz
~~~~

The **opencv_transcoder_vnf.tar.gz**, which is the VNF Descriptor.
The **opencv_transcoder_ns.tar.gz**, which is the NS Descriptor.

After they are built, you can upload them to OSM to be used.

## Configuring the OpenCV Transcoder VNF

After the VNF is launched, you must configure the source of the video stream and output port via OSM. The stream ip value you must pass is the complete URL.
