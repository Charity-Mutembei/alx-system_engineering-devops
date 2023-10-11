# Define a Puppet resource to
# create the missing configuration file

# Troubleshoot Apache's 500 error by examining its behavior with strace.

exec {'Fixer':
  command => "strace -f -e trace=file -o /path/to/output.log /usr/sbin/apache2",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}