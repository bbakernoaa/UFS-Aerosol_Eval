"""
Plot the Giorgi region definitions included in MM
"""
import cartopy.crs as ccrs
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from melodies_monet.util.tools import get_giorgi_region_bounds

plt.close("all")

#
# Get the MM Giorgi regions
#

imin, imax = 1, 22
data = []
for i in range(imin, imax+1):
    lst = get_giorgi_region_bounds(index=i)
    data.append(lst)
assert get_giorgi_region_bounds(index=imin-1).size == 0
assert get_giorgi_region_bounds(index=imax+1).size == 0
columns = "latmin, lonmin, latmax, lonmax, acro".split(", ")
df = pd.DataFrame(data, columns=columns, index=pd.RangeIndex(imin, imax+1))

# https://github.com/regionmask/regionmask/blob/f2147f082eaba150d124a9fa639c945855006a80/regionmask/defined_regions/giorgi.py#L51
names = dict()
names["AUS"] = "Australia"
names["AMZ"] = "Amazon Basin"
names["SSA"] = "Southern South America"
names["CAM"] = "Central America"
names["WNA"] = "Western North America"
names["CNA"] = "Central North America"
names["ENA"] = "Eastern North America"
names["ALA"] = "Alaska"
names["GRL"] = "Greenland"
names["MED"] = "Mediterranean Basin"
names["NEU"] = "Northern Europe"
names["WAF"] = "Western Africa"
names["EAF"] = "Eastern Africa"
names["SAF"] = "Southern Africa"
names["SAH"] = "Sahara"
names["SEA"] = "Southeast Asia"
names["EAS"] = "East Asia"
names["SAS"] = "South Asia"
names["CAS"] = "Central Asia"
names["TIB"] = "Tibet"
names["NAS"] = "North Asia"

# Additional ones not in the regionmask Giorgi
names["NAU"] = "Northern Australia"
names["SAU"] = "Southern Australia"

# Add names to df
df["name"] = df.acro.apply(lambda x: names.get(x, "?"))

print(df)

#
# Plot
#

clon = 2
proj = ccrs.Mercator(central_longitude=clon, min_latitude=-80.0, max_latitude=86.0)
tran = ccrs.PlateCarree()

fig, ax = plt.subplots(subplot_kw=dict(projection=proj))

ax.coastlines(resolution="110m", lw=1, color="0.5", zorder=0)
ax.set_extent([-180 + clon, 179 + clon, -60, 80], crs=tran)
# NOTE: max latmax is 85, max lonmax is 180

# We will offset some labels so that we can read them better
xoff = {
    "WNA": -10,
    "ENA": 12,
}
yoff = {
    "WNA": 3,
    "SAU": -1,
    "SAH": -1,
}

def plot_region(row):
    x = row.lonmin
    y = row.latmin
    w = row.lonmax - row.lonmin
    h = row.latmax - row.latmin
    assert w > 0 and h > 0
    p = mpl.patches.Rectangle((x, y), w, h,
        lw=2, ec="0.3", fc="none",
        transform=tran,
    )
    ax.add_patch(p)
    xc = x + w/2 + xoff.get(row.acro, 0)
    yc = y + h/2 + yoff.get(row.acro, 0)
    # TODO: at higher lats, currently not centered in y since projection
    ax.text(xc, yc, row.acro,
        va="center", ha="center",
        transform=tran,
        bbox=dict(boxstyle="round", fc="0.8", ec="none", mutation_aspect=0.7, alpha=0.9),
        size=16,
    )

# Label lat/lon a bit
kw = dict(c="0.5", ls="--", zorder=1, lw=1)
ax.axhline(0, **kw)
ax.axvline(0, **kw)
kw = dict(transform=tran, c="0.53", va="bottom", ha="left")
ex = ax.get_extent(crs=tran)
ax.text(ex[0] + 3, 0, "0°N", **kw)
ax.text(0 + 3.5, ex[2], "0°E", **kw)
# NOTE: `ha="left"` not working well so added padding

df.apply(plot_region, axis=1)

fig.tight_layout()

plt.show()

kw = dict(bbox_inches="tight", pad_inches=0.05)
fig.savefig("mm-giorgi.png", dpi=200, **kw)
fig.savefig("mm-giorgi.svg", transparent=True, **kw)
