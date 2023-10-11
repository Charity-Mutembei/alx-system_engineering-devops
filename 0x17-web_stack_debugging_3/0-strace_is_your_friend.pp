# Define a Puppet resource to
# create the missing configuration file

exec { 'diagnose_apache_issue':
command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
path    => ['/usr/bin/', '/usr/local/bin/', '/bin/'],
}
