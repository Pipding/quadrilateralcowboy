# utility module to process incoming GL description

import sys, string

def read_gl(f_in):
	buffer = f_in.read()
	lines = buffer.splitlines()

	gl = []
	wgl = []
	glX = []

	for line in lines:
		if ( len(line) ): # drop empty lines
			tokens = line.split(';')
			if ( tokens[1] == 'qgl' ):
				gl.append(tokens)
			elif ( tokens[1] == 'qwgl' ):
				wgl.append(tokens)
			elif ( tokens[1] == 'qglX' ):
				glX.append(tokens)
			else:
				sys.stderr.write('ERROR: unknown type %s\n' % tokens[1])
				raise "abort"
	
	return (gl, wgl, glX)
