pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'gtkworkshop')
gnome = import('gnome')

python3 = import('python3')

conf = configuration_data()
conf.set('PYTHON', python3.find_python().path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'gtkworkshop.in',
  output: 'gtkworkshop',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

gtkworkshop_sources = [
  '__init__.py',
  'MyWindow.py',
  'main.py',
  'lesson1.py',
  'lesson2.py',
  'lesson3.py',
  'lesson4.py',
  'lesson5.py',
  'lesson6.py',
  'lesson7.py',
  
  'project/project.py',
  'project/MyMainBox.py',
  'project/MyFileChooser.py',
  'project/MyButtons.py',
  'project/MyHeaderBar.py'
]

install_data(gtkworkshop_sources, install_dir: moduledir)