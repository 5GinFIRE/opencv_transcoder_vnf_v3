pipeline {
    agent { dockerfile true }

    parameters {
       string(defaultValue: 'opencv_transcoder_vnfd', description: 'name of the vnf', name: 'nameVNFD')
       string(defaultValue: 'opencv', description: 'name of the charm', name: 'charm')
   }

    stages {
        stage('Fetching Scripts') {
          steps {
            sh 'rm -rf devops'
            echo 'Fetching scripts'
            sh 'git clone https://osm.etsi.org/gerrit/osm/devops.git'
          }
        }
        stage('Test Descriptor') {
          steps {
            echo 'Testing before building'
            sh 'chmod +x ./devops/descriptor-packages/tools/upgrade_descriptor_version.py'
            sh './devops/descriptor-packages/tools/upgrade_descriptor_version.py --test vnf/opencv_transcoder_vnfd.yaml'
          }
        }
        //think about how to build many charms
        //not being able to install snapd
        /*
        stage('Build charm') {
          steps {
            echo 'Building charms'
            sh 'cd charms/transcoder'
            sh 'charm build'
          }
        }*/
        stage('Build Package') {
            steps {
                echo 'Generating VNF'
                /* vnf on rep with the same name of the created? */
                /*sh './devops/descriptor-packages/tools/generate_descriptor_pkg.sh -t vnfd --image noImage -c opencv_transcoder'
                echo 'Copying yaml'
                sh 'mv opencv_transcoder_test_vnfd/opencv_transcoder_test_vnfd.yaml opencv_transcoder_vnfd/opencv_transcoder_vnfd.yaml'
                */
                sh 'cp -R charms/$charm vnf/charms'

                // multiple charms? don't know number of variables to create
                echo 'Creating tar gz file'
                sh './devops/descriptor-packages/tools/generate_descriptor_pkg.sh -t vnfd -N vnf/$nameVNFD'
            }
        }

    }
}
