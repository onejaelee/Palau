import copernicus_marine_client as copernicusmarine

maxlat = 15
minlat = 0
minlon = 125
maxlon = 140

start_date_str = "1993-01-01T00:00:00"
end_date_str = "2023-04-30T23:59:59"
data_dir = "../data"

"""
Retrieves Copernicus Marine data for a specified region and time period.

Args:
    minlon (float): Minimum longitude of the region.
    maxlon (float): Maximum longitude of the region.
    minlat (float): Minimum latitude of the region.
    maxlat (float): Maximum latitude of the region.
    start_date_str (str): Start date of the data in ISO 8601 format.
    end_date_str (str): End date of the data in ISO 8601 format.
    data_dir (str): Directory to save the retrieved data.

Returns:
    str: The filename of the retrieved data.
"""
copernicusmarine.subset(
    dataset_id="cmems_obs-sl_glo_phy-ssh_my_allsat-l4-duacs-0.25deg_P1D",
    variables=["adt", "sla"],
    minimum_longitude=minlon,
    maximum_longitude=maxlon,
    minimum_latitude=minlat,
    maximum_latitude=maxlat,
    start_datetime=start_date_str,
    end_datetime=end_date_str,
    output_directory=data_dir,
    output_filename="cmems_L4_SSH_0.25deg_" + start_date_str[0:4] + "_" + end_date_str[0:4] + ".nc"
)

