# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
  listen 80;
  server_name localhost;

  location / {
    root   /var/www/html;
    index  index.html;
    try_files \$uri \$uri/ =404;
  }

  location /redirect_me {
    rewrite ^ http://example.com/new_location permanent;
  }
}
",
  notify => Service['nginx'],
}

# Create Hello World page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Enable and start Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
