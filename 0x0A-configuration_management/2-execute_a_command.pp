# Manifest for Killing a Process named `killmenow`
exec { 'kill_killmenow_process':
  command => 'pkill -9 killmenow)',
  path => '/usr/bin:/usr/local/bin',
  onlyif => 'pgrep killmenow',
}
