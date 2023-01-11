# Manifest for Killing a Process named `killmenow`
exec { 'kill_killmenow_process':
  command => 'kill -9 $(pgrep killmenow)',
  path => '/',
  onlyif => 'pgrep killmenow',
}
