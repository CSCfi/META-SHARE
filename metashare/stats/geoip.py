# List of country codes (indexed by GeoIP country ID number)
countries = (
	'',	  'AP', 'EU', 'AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ',
	'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH',
	'BI', 'BJ', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA',
	'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU',
	'CV', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG',
	'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'FX', 'GA', 'GB',
	'GD', 'GE', 'GF', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT',
	'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN',
	'IO', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM',
	'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS',
	'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN',
	'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA',
	'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA',
	'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY',
	'QA', 'RE', 'RO', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI',
	'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SY', 'SZ', 'TC', 'TD',
	'TF', 'TG', 'TH', 'TJ', 'TK', 'TM', 'TN', 'TO', 'TL', 'TR', 'TT', 'TV', 'TW',
	'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN',
	'VU', 'WF', 'WS', 'YE', 'YT', 'RS', 'ZA', 'ZM', 'ME', 'ZW', 'A1', 'A2', 'O1',
	'AX', 'GG', 'IM', 'JE', 'BL', 'MF')

# List of country info
country_info = {"A1": ["Anonymous Proxy", ""],
"A2": ["Satellite Provider", ""],
"O1": ["Other Country", ""],
"AD": ["Andorra", "42.5075314,1.5218156"],
"AE": ["United Arab Emirates", "23.424076,53.847818"],
"AF": ["Afghanistan", "33.0,66.0"],
"AG": ["Antigua and Barbuda", "17.060816,-61.796428"],
"AI": ["Anguilla", "18.21667,-63.05"],
"AL": ["Albania", "41.0,20.0"],
"AM": ["Armenia", "40.069099,45.038189"],
"AO": ["Angola", "-12.5,18.5"],
"AP": ["Asia/Pacific Region", "28.5396421,77.293131"],
"AQ": ["Antarctica", "-90.0,0.0"],
"AR": ["Argentina", "-34.0,-64.0"],
"AS": ["American Samoa", "-14.270972,-170.132217"],
"AT": ["Austria", "47.516231,14.550072"],
"AU": ["Australia", "-25.0,135.0"],
"AW": ["Aruba", "12.5,-69.96667"],
"AX": ["Aland Islands", "60.25,20.0"],
"AZ": ["Azerbaijan", "40.143105,47.576927"],
"BA": ["Bosnia and Herzegovina", "43.915886,17.679076"],
"BB": ["Barbados", "25.04082,-77.37122"],
"BD": ["Bangladesh", "24.0,90.0"],
"BE": ["Belgium", "50.83333,4.0"],
"BF": ["Burkina Faso", "12.238333,-1.561593"],
"BG": ["Bulgaria", "42.733883,25.48583"],
"BH": ["Bahrain", "25.930414,50.637772"],
"BI": ["Burundi", "-3.373056,29.918886"],
"BJ": ["Benin", "9.5,2.25"],
"BL": ["Saint Bartelemey", "17.90,-62.82"],
"BM": ["Bermuda", "32.281074,-64.7784787"],
"BN": ["Brunei Darussalam", "4.535277,114.727669"],
"BO": ["Bolivia", "-17.0,-65.0"],
"BQ": ["Bonaire, Saint Eustatius and Saba", "12.21286,-68.29445"],
"BR": ["Brazil", "-10.0,-55.0"],
"BS": ["Bahamas", "25.03428,-77.39628"],
"BT": ["Bhutan", "27.5,90.5"],
"BV": ["Bouvet Island", "-3.373056,29.918886"],
"BW": ["Botswana", "-22.328474,24.684866"],
"BY": ["Belarus", "53.709807,27.953389"],
"BZ": ["Belize", "17.25,-88.75"],
"CA": ["Canada", "60.10867,-113.64258"],
"CC": ["Cocos (Keeling) Islands", "-12.0,96.83333"],
"CD": ["The Democratic Republic of the Congo", "-4.038333,21.758664"],
"CF": ["Central African Republic", "6.611111,20.939444"],
"CG": ["Congo", "-4.038333,21.758664"],
"CH": ["Switzerland", "46.818188,8.227512"],
"CI": ["Cote d'Ivoire", "7.539989,-5.54708"],
"CK": ["Cook Islands", "-21.236736,-159.777671"],
"CL": ["Chile", "-30.0,-71.0"],
"CM": ["Cameroon", "6.0,12.0"],
"CN": ["China", "35.0,105.0"],
"CO": ["Colombia", "4.570868,-74.297333"],
"CR": ["Costa Rica", "10.0,-84.0"],
"CU": ["Cuba", "22.0,-79.5"],
"CV": ["Cape Verde", "16.002082,-24.013197"],
"CW": ["Curacao", "12.16667,-69.0"],
"CX": ["Christmas Island", "-10.5,105.66667"],
"CY": ["Cyprus", "35.126413,33.429859"],
"CZ": ["Czech Republic", "49.817492,15.472962"],
"DE": ["Germany", "51.5,10.5"],
"DJ": ["Djibouti", "11.5,42.5"],
"DK": ["Denmark", "56.26392,9.501785"],
"DM": ["Dominica", "15.5,-61.33333"],
"DO": ["Dominican Republic", "18.735693,-70.162651"],
"DZ": ["Algeria", "28.0,3.0"],
"EC": ["Ecuador", "-2.0,-77.5"],
"EE": ["Estonia", "58.595272,25.013607"],
"EG": ["Egypt", "27.0,30.0"],
"EH": ["Western Sahara", "24.215527,-12.885834"],
"ER": ["Eritrea", "15.0,39.0"],
"ES": ["Spain", "40.463667,-3.74922"],
"ET": ["Ethiopia", "8.0,38.0"],
"EU": ["Europe", "48.69096,9.14062"],
"FI": ["Finland", "64.0,26.0"],
"FJ": ["Fiji", "-18.0,178.0"],
"FK": ["Falkland Islands (Malvinas)", "-51.796253,-59.523613"],
"FM": ["Federated States of Micronesia", "6.924,158.162"],
"FO": ["Faroe Islands", "62.0,-7.0"],
"FR": ["France", "46.0,2.0"],
"GA": ["Gabon", "-1.0,11.75"],
"GB": ["United Kingdom", "55.378051,-3.435973"],
"GD": ["Grenada", "12.11667,-61.66667"],
"GE": ["Georgia", "42.315407,43.356892"],
"GF": ["French Guiana", "3.933889,-53.125782"],
"GG": ["Guernsey", "49.45853,-2.5787"],
"GH": ["Ghana", "8.1,-1.2"],
"GI": ["Gibraltar", "36.15122,-5.34966"],
"GL": ["Greenland", "72.0,-40.0"],
"GM": ["Gambia", "13.443182,-15.310139"],
"GN": ["Guinea", "9.945587,-9.696645"],
"GP": ["Guadeloupe", "16.25939,-61.55111"],
"GQ": ["Equatorial Guinea", "1.650801,10.267895"],
"GR": ["Greece", "39.0,22.0"],
"GS": ["South Georgia and the South Sandwich Islands", "-54.429579,-36.587909"],
"GT": ["Guatemala", "15.5,-90.25"],
"GU": ["Guam", "13.481,144.732"],
"GW": ["Guinea-Bissau", "12.0,-15.0"],
"GY": ["Guyana", "5.0,-59.0"],
"HK": ["Hong Kong", "22.2478599,114.2033843"],
"HM": ["Heard Island and McDonald Islands", "-53.08181,73.504158"],
"HN": ["Honduras", "15.199999,-86.241905"],
"HR": ["Croatia", "45.1,15.2"],
"HT": ["Haiti", "19.0,-72.41667"],
"HU": ["Hungary", "47.0,20.0"],
"ID": ["Indonesia", "-5.0,120.0"],
"IE": ["Ireland", "53.0,-8.0"],
"IL": ["Israel", "31.5,34.75"],
"IM": ["Isle of Man", "54.25,-4.5"],
"IN": ["India", "20.0,77.0"],
"IO": ["British Indian Ocean Territory", "-6.343194,71.876519"],
"IQ": ["Iraq", "33.0,44.0"],
"IR": ["Islamic Republic of Iran", "32.0,53.0"],
"IS": ["Iceland", "65.0,-18.0"],
"IT": ["Italy", "42.83333,12.83333"],
"JE": ["Jersey", "49.2167,-2.13753"],
"JM": ["Jamaica", "18.25,-77.5"],
"JO": ["Jordan", "31.0,36.0"],
"JP": ["Japan", "35.68536,139.75309"],
"KE": ["Kenya", "1.0,38.0"],
"KG": ["Kyrgyzstan", "41.0,75.0"],
"KH": ["Cambodia", "13.0,105.0"],
"KI": ["Kiribati", "1.421,172.984"],
"KM": ["Comoros", "-11.927966,43.478654"],
"KN": ["Saint Kitts and Nevis", "17.357822,-62.782998"],
"KP": ["Democratic People's Republic of Korea", "40.0,127.0"],
"KR": ["Republic of Korea", "35.907757,127.766922"],
"KW": ["Kuwait", "29.5,47.75"],
"KY": ["Cayman Islands", "19.5,-80.66667"],
"KZ": ["Kazakhstan", "48.0,68.0"],
"LA": ["Lao People's Democratic Republic", "18.0,105.0"],
"LB": ["Lebanon", "33.83333,35.83333"],
"LC": ["Saint Lucia", "13.909444,-60.978893"],
"LI": ["Liechtenstein", "47.16667,9.53333"],
"LK": ["Sri Lanka", "7.5,80.5"],
"LR": ["Liberia", "6.5,-9.5"],
"LS": ["Lesotho", "-29.5,28.25"],
"LT": ["Lithuania", "56.0,24.0"],
"LU": ["Luxembourg", "49.75,6.16667"],
"LV": ["Latvia", "57.0,25.0"],
"LY": ["Libyan Arab Jamahiriya", "31.767,13.983"],
"MA": ["Morocco", "32.0,-5.0"],
"MC": ["Monaco", "43.739104,7.423196"],
"MD": ["Republic of Moldova", "47.0,29.0"],
"ME": ["Montenegro", "42.5,19.3"],
"MF": ["Saint Martin", "18.05,-63.12"],
"MG": ["Madagascar", "-20.0,47.0"],
"MH": ["Marshall Islands", "6.06315,171.85596"],
"MK": ["Macedonia", "41.83333,22.0"],
"ML": ["Mali", "17.0,-4.0"],
"MM": ["Myanmar", "22.0,98.0"],
"MN": ["Mongolia", "46.0,105.0"],
"MO": ["Macao", "22.15778,113.55972"],
"MP": ["Northern Mariana Islands", "15.12,145.45"],
"MQ": ["Martinique", "14.66667,-61.0"],
"MR": ["Mauritania", "20.0,-12.0"],
"MS": ["Montserrat", "16.75,-62.2"],
"MT": ["Malta", "35.91667,14.43333"],
"MU": ["Mauritius", "-20.3,57.58333"],
"MV": ["Maldives", "3.2,73.0"],
"MW": ["Malawi", "-13.5,34.0"],
"MX": ["Mexico", "23.0,-102.0"],
"MY": ["Malaysia", "2.5,112.5"],
"MZ": ["Mozambique", "-18.25,35.0"],
"NA": ["Namibia", "-22.0,17.0"],
"NC": ["New Caledonia", "-22.16,166.27"],
"NE": ["Niger", "16.0,8.0"],
"NF": ["Norfolk Island", "-29.046,167.958"],
"NG": ["Nigeria", "10.0,8.0"],
"NI": ["Nicaragua", "13.0,-85.0"],
"NL": ["Netherlands", "52.5,5.75"],
"NO": ["Norway", "62.0,10.0"],
"NP": ["Nepal", "28.0,84.0"],
"NR": ["Nauru", "-0.517,166.933"],
"NU": ["Niue", "-19.03333,-169.86667"],
"NZ": ["New Zealand", "-40.900557,174.885971"],
"OM": ["Oman", "21.0,57.0"],
"PA": ["Panama", "9.0,-80.0"],
"PE": ["Peru", "-10.0,-76.0"],
"PF": ["French Polynesia", "-9.75,-139.0"],
"PG": ["Papua New Guinea", "-5.6,143.0"],
"PH": ["Philippines", "13.0,122.0"],
"PK": ["Pakistan", "30.0,70.0"],
"PL": ["Poland", "52.0,20.0"],
"PM": ["Saint Pierre and Miquelon", "46.50,-56.20"],
"PN": ["Pitcairn", "-24.407138,-128.320312"],
"PR": ["Puerto Rico", "18.15,-66.30"],
"PS": ["Palestinian Territory", "31.9465703,35.3027226"],
"PT": ["Portugal", "39.5,-8.0"],
"PW": ["Palau", "7.503,134.621"],
"PY": ["Paraguay", "-22.99333,-57.99639"],
"QA": ["Qatar", "25.5,51.25"],
"RE": ["Reunion", "-21.06,55.36"],
"RO": ["Romania", "46.0,25.0"],
"RS": ["Serbia", "44.81892,20.45998"],
"RU": ["Russian Federation", "61.52401,105.318756"],
"RW": ["Rwanda", "-2.0,30.0"],
"SA": ["Saudi Arabia", "23.885942,45.079162"],
"SB": ["Solomon Islands", "-9.64571,160.156194"],
"SC": ["Seychelles", "-4.58333,55.66667"],
"SD": ["Sudan", "16.0,30.0"],
"SE": ["Sweden", "62.0,15.0"],
"SG": ["Singapore", "1.36667,103.8"],
"SH": ["Saint Helena", "-15.9650104,-5.7089241"],
"SI": ["Slovenia", "46.25,15.16667"],
"SJ": ["Svalbard and Jan Mayen", "77.8749725,20.9751822"],
"SK": ["Slovakia", "48.66667,19.5"],
"SL": ["Sierra Leone", "8.5,-11.5"],
"SM": ["San Marino", "43.93333,12.41667 "],
"SN": ["Senegal", "14.0,-14.0"],
"SO": ["Somalia", "6.0,48.0"],
"SR": ["Suriname", "4.0,-56.0"],
"ST": ["Sao Tome and Principe", "0.18636,6.613081"],
"SV": ["El Salvador", "13.83333,-88.91667"],
"SX": ["Sint Maarten", "18.04167,-63.06667"],
"SY": ["Syrian Arab Republic", "33.5667,36.3667"],
"SZ": ["Swaziland", "-26.5,31.5"],
"TC": ["Turks and Caicos Islands", "21.783731,-71.770785"],
"TD": ["Chad", "15.0,19.0"],
"TF": ["French Southern Territories", "-49.350,70.217"],
"TG": ["Togo", "8.0,1.16667"],
"TH": ["Thailand", "15.0,100.0"],
"TJ": ["Tajikistan", "39.0,71.0"],
"TK": ["Tokelau", "-9.167,-171.83"],
"TL": ["Timor-Leste", "-8.538333,125.684444"],
"TM": ["Turkmenistan", "40.0,60.0"],
"TN": ["Tunisia", "34.0,9.0"],
"TO": ["Tonga", "-20.0,-175.0"],
"TR": ["Turkey", "39.05901,34.91155"],
"TT": ["Trinidad and Tobago", "11.2317706,-60.6981989"],
"TV": ["Tuvalu", "-7.109535,177.64933"],
"TW": ["Taiwan", "24.0,121.0"],
"TZ": ["United Republic of Tanzania", "-6.0,35.0"],
"UA": ["Ukraine", "49.0,32.0"],
"UG": ["Uganda", "2.0,33.0"],
"UM": ["United States Minor Outlying Islands", "14.85985,-175.693359"],
"US": ["United States", "37.09024,-95.712891"],
"UY": ["Uruguay", "-33.0,-56.0"],
"UZ": ["Uzbekistan", "41.70754,63.84911"],
"VA": ["Holy See (Vatican City State)", "41.902477,12.458206"],
"VC": ["Saint Vincent and the Grenadines", "13.267,-61.117"],
"VE": ["Venezuela", "8.0,-66.0"],
"VG": ["Virgin Islands, British", "18.426980,-64.630280"],
"VI": ["Virgin Islands, U.S.", "18.3330115,-64.9709803"],
"VN": ["Vietnam", "16.16667,107.83333"],
"VU": ["Vanuatu", "-16.0,167.0"],
"WF": ["Wallis and Futuna", "-13.3,-176.2"],
"WS": ["Samoa", "-13.8031,-172.17831"],
"YE": ["Yemen", "15.5,47.5"],
"YT": ["Mayotte", "-12.83333,45.16667"],
"ZA": ["South Africa", "-30.559482,22.937506"],
"ZM": ["Zambia", "-15.0,30.0"],
"ZW": ["Zimbabwe", "-19.0,29.0"]}


def iptonum(ipaddress):
    """Convert IP address string to 32-bit integer, or return None if IP is bad."""
    segments = ipaddress.split('.')
    if len(segments) != 4:
        return None
    num = 0
    for segment in segments:
        try:
            segment = int(segment)
        except ValueError:
            return None
        if segment < 0 or segment > 255:
            return None
        num = num << 8 | segment
    return num

class DatabaseError(Exception):
    pass

class GeoIP(object):
    """Wraps GeoIP country database lookup into a class."""
    _record_length = 3
    _country_start = 16776960
    
    def __init__(self, dbname='stats/resources/GeoIP.dat'):
        """Init GeoIP instance with given GeoIP country database file."""
        self._dbfile = open(dbname, 'rb')

    def country(self, ipaddress):
        ipnum = iptonum(ipaddress)
        if ipnum is None or ipaddress == "":
            return ''
        return countries[self._country_id(ipnum)]

    def _country_id(self, ipnum):
        """Look up and return country ID of given 32-bit IP address."""
        # Search algorithm from: http://code.google.com/p/pygeoip/
        offset = 0
        for depth in range(31, -1, -1):
            self._dbfile.seek(offset * 2 * self._record_length)
            data = self._dbfile.read(2 * self._record_length)
            coords = [0, 0]
            for i in range(2):
                for j in range(self._record_length):
                    coords[i] += ord(data[self._record_length * i + j]) << (j * 8)
            i = 1 if ipnum & (1 << depth) else 0
            if coords[i] >= self._country_start:
                return coords[i] - self._country_start
            offset = coords[i]
        raise DatabaseError('GeoIP database corrupt: offset=%s' % offset)
    
def getcountry_name(countryid):
    if countryid in country_info:
        return country_info[countryid][0]
    return "Other Country"

def getcountry_coords(countryid):
    if countryid in country_info:
        return country_info[countryid][1]
    return ""
        
def getcountry(ipaddress):
    return GeoIP().country(ipaddress)
    
