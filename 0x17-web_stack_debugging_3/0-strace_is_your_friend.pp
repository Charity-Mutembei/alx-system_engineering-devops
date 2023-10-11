# Define a Puppet resource to
# create the missing configuration file

exec { 'diagnose_apache_issue':
command     => 'strace -f -p <apache_process_id> 2>&1',
path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
refreshonly => true,
logoutput   => true,
unless      => 'grep -q "Specific Error Condition" /var/log/strace_output.log', # Replace with a unique error condition
notify      => Exec['fix_apache_issue'],
}
