# installing a package using puppet
   exec { 'install python packages':
    command   => 'pip3 install flask flask_restful apiai; touch /root/installed.txt',
    path      => ['/usr/bin/'],
    before    => Exec['create custom facter'],
  }
