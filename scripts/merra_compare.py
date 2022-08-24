#!/usr/bin/env python
import argparse
import pandas as pd
import xarray as xr
import os
import matplotlib.pyplot as plt
import numpy as np
import monet
import monetio
import seaborn as sns

class TaylorDiagram:
    """Taylor diagram: plot model standard deviation and correlation
    to reference (data) sample in a single-quadrant polar plot, with
    r=stddev and theta=arccos(correlation).
    """

    def __init__(self, refstd, scale=1.5, fig=None, rect=111, label="_"):
        """Set up Taylor diagram axes, i.e. single quadrant polar
        plot, using mpl_toolkits.axisartist.floating_axes. refstd is
        the reference standard deviation to be compared to.
        """

        import mpl_toolkits.axisartist.floating_axes as FA
        import mpl_toolkits.axisartist.grid_finder as GF
        from matplotlib.projections import PolarAxes

        self.refstd = refstd  # Reference standard deviation

        tr = PolarAxes.PolarTransform()

        # Correlation labels
        rlocs = np.concatenate((np.arange(10) / 10.0, [0.95, 0.99]))
        tlocs = np.arccos(rlocs)  # Conversion to polar angles
        gl1 = GF.FixedLocator(tlocs)  # Positions
        tf1 = GF.DictFormatter(dict(list(zip(tlocs, list(map(str, rlocs))))))

        # Standard deviation axis extent
        self.smin = 0
        self.smax = scale * self.refstd
        ghelper = FA.GridHelperCurveLinear(
            tr,
            extremes=(0, np.pi / 2, self.smin, self.smax),
            grid_locator1=gl1,
            tick_formatter1=tf1,
        )  # 1st quadrant

        if fig is None:
            fig = PLT.figure()

        ax = FA.FloatingSubplot(fig, rect, grid_helper=ghelper)
        fig.add_subplot(ax)

        # Adjust axes
        ax.axis["top"].set_axis_direction("bottom")  # "Angle axis"
        ax.axis["top"].toggle(ticklabels=True, label=True)
        ax.axis["top"].major_ticklabels.set_axis_direction("top")
        ax.axis["top"].label.set_axis_direction("top")
        ax.axis["top"].label.set_text("Correlation")

        ax.axis["left"].set_axis_direction("bottom")  # "X axis"
        ax.axis["left"].label.set_text("Standard deviation")

        ax.axis["right"].set_axis_direction("top")  # "Y axis"
        ax.axis["right"].toggle(ticklabels=True)
        ax.axis["right"].major_ticklabels.set_axis_direction("left")

        ax.axis["bottom"].set_visible(False)  # Useless

        # Contours along standard deviations
        ax.grid(False)

        self._ax = ax  # Graphical axes
        self.ax = ax.get_aux_axes(tr)  # Polar coordinates

        # Add reference point and stddev contour
        print("Reference std:", self.refstd)
        (l,) = self.ax.plot([0], self.refstd, "r*", ls="", ms=14, label=label, zorder=10)
        t = np.linspace(0, np.pi / 2)
        r = np.zeros_like(t) + self.refstd
        self.ax.plot(t, r, "k--", label="_")

        # Collect sample points for latter use (e.g. legend)
        self.samplePoints = [l]

    def add_sample(self, stddev, corrcoef, *args, **kwargs):
        """Add sample (stddev,corrcoeff) to the Taylor diagram. args
        and kwargs are directly propagated to the Figure.plot
        command."""
        (l,) = self.ax.plot(np.arccos(corrcoef), stddev, *args, **kwargs)  # (theta,radius)
        self.samplePoints.append(l)

        return l

    def add_contours(self, levels=5, **kwargs):
        """Add constant centered RMS difference contours."""

        rs, ts = np.meshgrid(np.linspace(self.smin, self.smax), np.linspace(0, np.pi / 2))
        # Compute centered RMS difference
        rms = np.sqrt(self.refstd**2 + rs**2 - 2 * self.refstd * rs * np.cos(ts))

        contours = self.ax.contour(ts, rs, rms, levels, **kwargs)

        return contours


def create_boxplot(p8c,p72,mer,title='AOD',ufs_var='AOD',merra_var='TOTEXTTAU', init_date=None):
    f = plt.figure(figsize=(20,7))
    p8cdf = p8c[ufs_var].to_dataframe().reset_index().rename(dict(lat='latitude',lon='longitude'),axis=1)
    p72df = p72[ufs_var].to_dataframe().reset_index().rename(dict(lat='latitude',lon='longitude'),axis=1)
    mdf = mer[merra_var].to_dataframe().reset_index().rename(dict(lat='latitude',lon='longitude'),axis=1)
    p8cdf = monet.util.get_giorgi_region_df(p8cdf)
    p72df = monet.util.get_giorgi_region_df(p72df)
    mdf = monet.util.get_giorgi_region_df(mdf).rename({merra_var:ufs_var},axis=1)
    p8cdf['model'] = 'P8C'
    p72df['model'] = 'P72'
    mdf['model'] = 'MERRA2'
    tdf = pd.concat([p8cdf[[ufs_var,'model','GIORGI_ACRO']],p72df[[ufs_var,'model','GIORGI_ACRO']]],ignore_index=True)
    tdf = pd.concat([tdf[[ufs_var,'model','GIORGI_ACRO']],mdf[[ufs_var,'model','GIORGI_ACRO']]],ignore_index=True)
    ax = sns.boxplot(x='GIORGI_ACRO',y=ufs_var,hue='model',data=tdf.loc[tdf.GIORGI_ACRO.isin(acro)],showfliers=False)
    
    plt.title('{} | {}'.format(ufs_var, init_date))
    plt.xlabel('')
    plt.tight_layout()
    return ax

def create_taylor(p8c,p72,mer,title='AOD'):
    merra_std = mer.std(ddof=1).compute()
    mstd = np.array([merra_std.values.tolist()])
    samples = np.array([[ model.values.std(ddof=1), np.corrcoef(mer.values.flatten(),model.values.flatten())[0,1]] for model in (p8c,p72)])
    fig = plt.figure(figsize=(10, 10))
    dia = TaylorDiagram(np.array([merra_std.values.tolist()]), scale=1.5, fig=fig, rect=111, label='MERRA2')
    dia.add_sample(samples[0][0], samples[0][1],marker='o',zorder=9, ls=None,label='P8C')
    dia.add_sample(samples[1][0], samples[1][1],marker='o',zorder=9, ls=None,label='P72')
    contours = dia.add_contours(colors="0.5")
    plt.clabel(contours, inline=1, fontsize=10)
    plt.grid(alpha=0.5)
    plt.legend(fontsize="small", loc="best")
    plt.title(title)
    plt.tight_layout()
    
def open_ufs(path):
    return xr.open_mfdataset(os.path.join(path,'gocart.inst_aod.*'))

def open_merra2(times):
    from glob import glob    
    merrafiles = np.sort(glob('MERRA2AOD/MERRA2_400.tavg1_2d_aer_Nx.2*.nc4'))
    merradf = pd.Series(merrafiles,index=pd.DatetimeIndex([get_merra2_times_from_file(fname) for fname in merrafiles]))
    mfiles = merradf.loc[times.min():times.max()]
    return xr.open_mfdataset(mfiles)

def get_merra2_times_from_file(fname):
    from datetime import datetime
    return datetime.strptime(fname.split('.')[-2],'%Y%m%d')

def regrid(u,m):
    import xesmf as xe
    regrid = xe.Regridder(m,u,'bilinear')
    merra_ufs = regrid(m)
#    ufs_merra = u.sel(time=merra_ufs.time) # match times 
    return merra_ufs

def create_bias_plot(a,b,name,title):
    difference = a - b
    difference.name=name
    levels=[-2,-1,-.5,-.4,-.3,-.2,-.1,-0.05,-.01,0.0,0.01,0.05,.1,.2,.3,.4,.5,1,2]
    difference.monet.quick_imshow(cmap='RdBu_r',levels=levels,cbar_kwargs={'ticks': levels},figsize=(14.5,6))
    plt.title(title)
    plt.tight_layout()
    
def get_giorgi_region(dset,region='SAH'):
    gbounds = monet.util.get_giorgi_region_bounds(acronym=region)
    return dset.sel(lat=slice(gbounds[0],gbounds[2]),lon=slice(gbounds[1],gbounds[3]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--p8c", action="store", required=True, type=str,
                        help="Start downloading data for this year")
    parser.add_argument("-m", "--merra", action="store", required=True, type=str,
                        help="End downloading data for this year")
    parser.add_argument("-p", "--p72", action="store", required=True, type=str,
                        help="End downloading data for this year")
    args = parser.parse_args()
    print(args)

    merra_species = ['TOTEXTTAU','BCEXTTAU','DUEXTTAU','OCEXTTAU','SSEXTTAU','SUEXTTAU']
    ufs_species = ['AOD', 'AOD_BC','AOD_DU','AOD_OC','AOD_SS','AOD_SU']
    
    
    p8c = open_ufs(args.p8c)
    p72 = open_ufs(args.p72).isel(lev=1)
    merra = open_merra2(p8c.time.to_dataframe().values).resample(time='6H').mean()
    merra = merra[merra_species]
    merra = regrid(p8c,merra)
    p8c_weekly = p8c.resample(time='7D').mean()
    p72_weekly = p72.resample(time='7D').mean()
    merra_weekly = merra.resample(time='7D').mean()
        
    # first create all the bias plots for each week
    initial_date = p8c.time.to_index().min().strftime('%Y%m%d00')

    acro = [
         "NAU",
         "SAU",
         "AMZ",
         "SSA",
         "CAM",
         "WNA",
         "CNA",
         "ENA",
         "ALA",
         "GRL",
         "MED",
         "NEU",
         "WAF",
         "EAF",
         "SAF",
         "SAH",
         "SEA",
         "EAS",
         "SAS",
         "CAS",
         "TIB",
         "NAS",
     ]
    # first global plots 
    for ufs_var,merra_var in zip(ufs_species,merra_species):
        print('Creating Taylor Plot All Times | Species {} ...'.format(ufs_var))
        create_taylor(p8c[ufs_var],p72[ufs_var],merra[merra_var],title='{} | {}'.format(ufs_var, initial_date))
        monet.savefig('{}/p8c_p72_merra2_taylor_{}_{}.jpg'.format(initial_date,initial_date,ufs_var),dpi=150)
        plt.close()

        print('Creating BoxPlot All Times | Species {} ...'.format(ufs_var))
        create_boxplot(p8c,p72,merra,title='{} | {}'.format(ufs_var,initial_date),ufs_var=ufs_var,merra_var=merra_var, init_date=initial_date)
        monet.savefig('{}/p8c_p72_merra2_boxplot_{}_{}.jpg'.format(initial_date,initial_date,ufs_var),dpi=150)
        plt.close()
        
        for i in range(4):
              print('Creating P8C Spatial Bias Plot Week {}...'.format(str(i+1)))
              title_string = 'Aerosol Optical Depth', 'P8C - MERRA2 | {} | Week {} | {}'.format(ufs_var, str(i+1), initial_date)
              create_bias_plot(p8c_weekly[ufs_var].isel(time=i), merra_weekly[merra_var].isel(time=i),ufs_var,title_string)
              monet.savefig('{}/p8c_merra2_bias_week{}_{}_{}.jpg'.format(initial_date,str(i+1),initial_date, ufs_var),dpi=150)
              title_string = 'Aerosol Optical Depth', 'P7.2 - MERRA2 | {} | Week {} | {}'.format(ufs_var, str(i+1), initial_date)
              plt.close()           
              
              print('Creating P72 Spatial Bias Plot Week {}...'.format(str(i+1)))
              create_bias_plot(p72_weekly[ufs_var].isel(time=i), merra_weekly[merra_var].isel(time=i),ufs_var, title=title_string)
              monet.savefig('{}/p72_merra2_bias_week{}_{}_{}.jpg'.format(initial_date,str(i+1),initial_date,ufs_var),dpi=150)
              plt.close()
              
              # create taylor diagrams
              print('Creating P8C Taylor Plot Week {}...'.format(str(i+1)))
              create_taylor(p8c_weekly[ufs_var].isel(time=i),
                            p72_weekly[ufs_var].isel(time=i),
                            merra_weekly[merra_var].isel(time=i),
                            title='{} | {} | {}'.format(ufs_var,initial_date, str(i+1)))
              monet.savefig('{}/p8c_p72_merra2_taylor_{}_{}_week{}.jpg'.format(initial_date,initial_date,ufs_var,str(i+1)),dpi=150)
              plt.close()
              
              print('Creating BoxPlot Week {} Species {}'.format(str(i+1),ufs_var))
              create_boxplot(p8c_weekly,p72_weekly,merra_weekly,title='{} | {} | Week {}'.format(ufs_var,initial_date,str(i+1)),ufs_var=ufs_var,merra_var=merra_var, init_date=initial_date)
              monet.savefig('{}/p8c_p72_merra2_boxplot_{}_week{}_{}.jpg'.format(initial_date,initial_date,str(i+1),ufs_var),dpi=150)
              plt.close()                                  
            
