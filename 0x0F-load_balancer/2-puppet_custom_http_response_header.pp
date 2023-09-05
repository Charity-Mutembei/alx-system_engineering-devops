# Define a class to manage the custom HTTP header
class custom_http_header {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/etc/nginx/sites-available/custom_http_header.conf':
    ensure  => 'present',
    content => "
      server_tokens off;

      location / {
          add_header X-Served-By $hostname;
          # Add other Nginx configuration here if needed
      }
    ",
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/custom_http_header.conf':
    ensure => 'link',
    target => '/etc/nginx/sites-available/custom_http_header.conf',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => [File['/etc/nginx/sites-available/custom_http_header.conf'], File['/etc/nginx/sites-enabled/custom_http_header.conf']],
  }
}

# Apply the class to the node
node default {
  class { 'custom_http_header': }
}