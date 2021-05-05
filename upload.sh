echo 'Removing old files....'
ssh root@192.168.122.24 'rm -rf /usr/share/cockpit/zfs'

echo 'Stopping cockpit....'
ssh root@192.168.122.24 'systemctl stop cockpit.socket'

echo 'Upload new files....'
rsync -r zfs/* root@192.168.122.24:/usr/share/cockpit/zfs

echo 'Starting cockpit....'
ssh root@192.168.122.24 'systemctl start cockpit.socket --now'