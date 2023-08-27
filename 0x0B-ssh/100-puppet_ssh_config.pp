#!/usr/bin/env bash
#configure private key
#refuse password for authentication
file { '~/.ssh/config':
  ensure => present,
  content => "# Managed by Puppet\n\nHost *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
}
