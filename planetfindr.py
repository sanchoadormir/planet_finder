import pyvo
from astropy.io.votable import parse

service = pyvo.dal.TAPService("http://voparis-tap-planeto.obspm.fr/tap")
while True:
	inf = input("Required info: ")
	inout = input("Conditions: ")
	query = "SELECT " + inf + " FROM exoplanet.epn_core WHERE " + inout
	results = service.search(query)
	parsedresults = str(len(results))
	print("There are  " + parsedresults + " planets fulfilling those conditions.")
	print(results)

"""
Available INFO and CONDITIONS

use *  for everything
target_name 
obs_id 
detection_type  (transit, RV, ...)
publication_status (refereed or not, published or not)
ra (deg) 
dec (deg) 
mass ('jupiterMass') mass_error_min mass_error_max 
radius ('jupiterRad')  radius_error_min radius_error_max 
mass_sin_i ('jupiterMass') mass_sin_i_error_min  mass_sin_i_error_max 
semi_major_axis (AU)  semi_major_axis_error_min  semi_major_axis_error_max
period (d)  period_error_min  period_error_max 
eccentricity  eccentricity_error_min  eccentricity_error_max 
discovered (the year of discovery)
angular_distance (arcsec) 
mass_detection_type 
radius_detection_type 
alt_target_name (alternate names of planets)
star_name 
star_distance (pc)  star_distance_error_min  star_distance_error_max 
star_spec_type  (Spectral types of the host stars)
mag_v  mag_i  mag_j  mag_h  mag_k  (magnitudes of the host stars in band V, I, J, H and K)
star_metallicity 
star_mass (solar Mass) 
star_radius (solar Radius) 
star_age (Gyr) 
star_teff (K) 
detected_disc (when a disc is detected, this field is filled in with the disc detection method)
creation_date 
modification_date 
species (the species detected in the planet's atmosphere)
temp_calculated (K)
temp_measured (K) 
log_g (of the planet) 
albedo  albedo_error_min  albedo_error_max 
updated (last update of the parameters)
remarks (some comments about a specific system)
other_web (some links to data when available)
periastron (deg)  periastron_error_min periastron_error_max (argument of periastron)
t_peri (d)  t_peri_error_min  t_peri_error_max  (epoch of periastron)
tzero_tr (d)  tzero_tr_error_min  tzero_tr_error_max  (epoch of primary transit)
tzero_vr (d)  tzero_vr_error_min  tzero_vr_error_max  (epoch of zero radial velocity)
t_conj (d)  t_conj_error_min  t_conj_error_max  (epoch of conjunction)
inclination (deg)  inclination_error_min  inclination_error_max (orbital inclination)
tzero_tr_sec (d)  tzero_tr_sec_error_min tzero_tr_sec_error_max (epoch of secondary transit)
lambda_angle (deg)  lambda_angle_error_min  lambda_angle_error_max (Sky-projected angle between the planetary orbital planet and the stellar rotational spin)
k (m/s)  k_error_min  k_error_max (Velocity semi-amplitude)
impact_parameter  impact_parameter_error_min  impact_parameter_error_max 
magnetic_field (say Yes if a magnetic field is detected)
"""
