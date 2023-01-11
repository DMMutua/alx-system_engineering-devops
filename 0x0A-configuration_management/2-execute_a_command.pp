# Manifest for Killing a Process named `killmenow`
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow)',
}
