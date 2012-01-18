import pyfits


def get_data():
    datafile = pyfits.open('ondelettes/data/ngc2997.fits')
    return datafile[0].data
