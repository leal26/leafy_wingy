import subprocess as sp

from xfoil_module import output_reader

def generate_venation(kill_distance, growth_distance, grid_size,
                      plot=False):
    """ Call xfoil through Python.

    @author: Pedro Leal (Based on Hakan Tiftikci's code)
    """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #                               Functions
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def issueCmd(cmd, echo=True):
        """Submit a command through PIPE to the command line, therefore
        leading the commands to xfoil.

        @author: Hakan Tiftikci
        """

        ps.stdin.write(cmd + '\n')
        if echo:
            print cmd

    # console-window-with-pyw-file-containing-os-system-call

    # Random output variable to avoid writing stuff from xfoil on the
    # console
    sout = 0
    # Calling xfoil with Poper
    if plot:
        ps = sp.Popen(['leafy_generator.exe'],
                      stdin=sp.PIPE,
                      stdout=sout,
                      stderr=None)
    else:
        startupinfo = sp.STARTUPINFO()
        startupinfo.dwFlags |= sp.STARTF_USESHOWWINDOW
        ps = sp.Popen(['leafy_generator.exe'],
                      stdin=sp.PIPE,
                      stdout=sout,
                      stderr=None,
                      startupinfo = startupinfo)
    # Kill distance
    issueCmd('%f' % kill_distance)
    # Growth distance
    issueCmd('%f' % growth_distance)
    # Grid size
    issueCmd('%f' % grid_size)
    # From stdin
    ps.stdin.close()
    # From popen
    ps.wait()

if __name__ == '__main__':
    generate_venation(.01, .01, 10, plot=True)

    header = ['element', 'x1', 'y1', 'x2', 'y2']
    structure = [['element'], ['x1', 'y1'], ['x2', 'y2']]
    Data = output_reader('edges.txt', header = header, structure = structure)

    # generate_venation(Data)
