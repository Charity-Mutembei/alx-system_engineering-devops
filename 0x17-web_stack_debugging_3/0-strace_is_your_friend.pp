# Define a Puppet resource to
# create the missing configuration file

exec {'Fixer':
  command => "strace -f -e trace=file -o /path/to/output.log /usr/sbin/apache2",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
