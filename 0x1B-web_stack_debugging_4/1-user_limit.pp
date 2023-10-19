# Define the user whose file limit needs to be adjusted
$target_user = 'holberton'

# Define the desired file descriptor limit
$file_limit = 10000

# Create the user
user { $target_user:
  ensure     => 'present',
  managehome => false,
  shell      => '/bin/bash',
  home       => "/home/${target_user}",
  uid        => undef,
  gid        => undef,
  groups     => [],
  allowdupe  => false,
  system     => false,
  password   => '*',
  expiry     => 'absent',
}

# Set ulimit for the user
exec { "Set ulimit for ${target_user}":
  command   => "ulimit -n ${file_limit}",
  path      => '/bin:/usr/bin',
  user      => $target_user,
  logoutput => true,
  require   => User[$target_user],
}
