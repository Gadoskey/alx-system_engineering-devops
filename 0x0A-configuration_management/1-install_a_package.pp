 # Ensure the python3-pip package is installed

class flask {
  package { 'python3-pip':
    ensure => installed,
  }

# Install the Flask package using pip3 with the specified version

exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    unless  => '/usr/bin/pip3 show flask | grep -q "^Version: 2.1.0"',
    require => Package['python3-pip'],
  }
}
