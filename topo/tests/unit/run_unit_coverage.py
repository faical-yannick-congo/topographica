import nose, sysif __name__ == '__main__':    nose.run(argv=["nosetests",					"--with-doctest",					"--doctest-extension=txt",					"--with-coverage",					"--cover-erase",					"--cover-html",					"--cover-html-dir=coverage_unit",					"--cover-package=topo.analysis",					"--cover-package=topo.base",					"--cover-package=topo.command",					"--cover-package=topo.coordmapper",					"--cover-package=topo.ep",					"--cover-package=topo.learningfn",					"--cover-package=topo.misc",					"--cover-package=topo.plotting",					"--cover-package=topo.projection",					"--cover-package=topo.responsefn",					"--cover-package=topo.sheet",					"--cover-package=topo.transferfn",					"--cover-package=param"					"--cover-branches"					])