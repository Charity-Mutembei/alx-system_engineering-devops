# Class: profile::user_limits
#
# This class configures user limits for the holberton user.
#
# Parameters:
# - $target_user: The target user for which limits will be set. Default: 'holberton'
# - $file_limit: The desired file descriptor limit. Default: 10000
#

class user_limits {
  # Define the user whose file limit needs to be adjusted
  $target_user = 'holberton'

  # Define the desired file descriptor limit
  $file_limit = 10000

  # Set file descriptor limits for the user
  user { $target_user:
    ensure     => 'present',
    managehome => false, # This assumes home directory already exists
    shell      => '/bin/bash',
    home       => "/home/${target_user}",
    uid        => undef,  # Use system-assigned UID
    gid        => undef,  # Use system-assigned GID
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
}

include user_limits
