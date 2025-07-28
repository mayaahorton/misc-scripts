import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy import units as u

def load_catalog(path):
    """Load a CSV catalog with RA, Dec columns."""
    return pd.read_csv(path)

def skycoord_from_dataframe(df, ra_col='RA', dec_col='Dec'):
    """Create a SkyCoord object from a DataFrame."""
    return SkyCoord(ra=df[ra_col].values * u.deg,
                    dec=df[dec_col].values * u.deg,
                    frame='icrs')

def deduplicate_catalogs(catalogs, threshold_arcsec=1.0):
    """Deduplicate sources across multiple catalogs."""
    all_coords = []
    all_dfs = []
    for df in catalogs:
        all_dfs.append(df)
        all_coords.append(skycoord_from_dataframe(df))

    # Combine all coordinates and indexes
    combined_coords = all_coords[0]
    combined_df = all_dfs[0]
    
    for i in range(1, len(all_coords)):
        match_idx, sep2d, _ = all_coords[i].match_to_catalog_sky(combined_coords)
        mask_new = sep2d > threshold_arcsec * u.arcsec
        
        df_new = all_dfs[i][mask_new]
        combined_df = pd.concat([combined_df, df_new], ignore_index=True)
        combined_coords = skycoord_from_dataframe(combined_df)

    return combined_df

if __name__ == "__main__":
    # Example usage
    cat1 = load_catalog("field1.csv")
    cat2 = load_catalog("field2.csv")
    cat3 = load_catalog("field3.csv")

    deduped = deduplicate_catalogs([cat1, cat2, cat3], threshold_arcsec=1.5)
    deduped.to_csv("deduplicated_catalog.csv", index=False)
