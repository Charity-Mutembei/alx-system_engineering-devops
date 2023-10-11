# Create a Puppet manifest to fix the Apache 500 error

# Ensure the wp-settings.php file exists
file { '/var/www/html/wp-settings.php':
ensure => file,
mode   => '0644',
}

# Define an Exec resource to replace the string using Puppet
exec { 'fix_wp_settings_php':
command     => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
path        => ['/usr/bin', '/usr/local/bin', '/bin'],
refreshonly => true,
subscribe   => File['/var/www/html/wp-settings.php'],
}
