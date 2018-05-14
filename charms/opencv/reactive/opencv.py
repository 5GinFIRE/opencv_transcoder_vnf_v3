import sys
import traceback
import charms.sshproxy

from charmhelpers.core.hookenv import (
    action_get,
    action_fail,
    action_set,
    status_set,
)

from charms.reactive import (
    remove_state as remove_flag,
    set_state as set_flag,
    when,
    when_not,
)


@when_not('opencv.installed')
def install_opencv():
    set_flag('opencv.installed')
    status_set('active', 'Ready!')

@when('actions.start-transcoder')
def start_transcoder():
    try:
        stream_ip = action_get('stream-ip')
        output_port = action_get('output-port')

        cmd = "sudo rm /etc/systemd/system/opencv.service >/dev/null 2>&1; "
        cmd += "sudo systemctl stop opencv.service >/dev/null 2>&1; "
        cmd += "sudo systemctl daemon-reload"
        charms.sshproxy._run(cmd)
    
        cmd = "echo '[Unit]' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'Description=OpenCV' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '[Service]' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'Type=simple' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'User=ubuntu' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'WorkingDirectory=/home/ubuntu' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'ExecStart=/usr/bin/python live_server.py {0} {1}' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && ".format(stream_ip, output_port)
        cmd += "echo 'Restart=always' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'RestartSec=5' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '[Install]' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'WantedBy=multi-user.target' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "sudo systemctl daemon-reload && "
        cmd += "sudo systemctl start opencv.service"
        result, _ = charms.sshproxy._run(cmd)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = traceback.format_exception(exc_type, exc_value, exc_traceback)
        action_fail('Starting transcoder failed: ' + str(err))
    else:
        action_set({'output': result})
    finally:
        remove_flag('actions.start-transcoder')
