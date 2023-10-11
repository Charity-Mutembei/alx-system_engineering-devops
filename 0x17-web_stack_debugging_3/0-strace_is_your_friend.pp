# Define a Puppet resource to
# create the missing configuration file

exec { 'diagnose_apache_issue':
command => 'strace -f -p <apache_process_id> 2>&1',
path    => ['/usr/bin/', '/usr/local/bin/', '/bin/'],
}
