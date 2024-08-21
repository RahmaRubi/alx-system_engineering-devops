#Increase Requests

exec { 'command':
  command  => '
  sed -i "s/5/5000/g" /etc/security/limits.conf
  sed -i "s/4/5000/g" /etc/security/limits.conf',
  provider => shell,
  }
