import matplotlib as mpl

def set_vis_params():
    mpl.rcParams.update({'font.size': 14})
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['axes.linewidth'] = 2

    mpl.rcParams['xtick.major.size'] = 8
    mpl.rcParams['xtick.major.width'] = 2
    mpl.rcParams['xtick.minor.size'] = 2
    mpl.rcParams['xtick.minor.width'] = 1

    mpl.rcParams['ytick.major.size'] = 8
    mpl.rcParams['ytick.major.width'] = 2
    mpl.rcParams['ytick.minor.size'] = 2
    mpl.rcParams['ytick.minor.width'] = 1

    mpl.rcParams['xtick.major.pad'] = '8'
    mpl.rcParams['ytick.major.pad'] = '8'